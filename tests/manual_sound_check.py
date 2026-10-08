# Plays through the Sound API so you can check it by ear. Not run by tox.
#
#     python tests/manual_sound_check.py          # generated tones
#     python tests/manual_sound_check.py --url    # also an mp3 over the network
#
# Each step prints what you should hear before it plays.

import argparse
import functools
import math
import os
import struct
import sys
import tempfile
import time
import wave

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from cmu_graphics import *  # noqa: E402, F403

# os._exit at the end skips flushing, so don't buffer
print = functools.partial(print, flush=True)

MP3_URL = 'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Liberty_bell_march.mp3'


def write_tone(path, frequency, seconds):
    rate = 22050
    with wave.open(path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(
            b''.join(
                struct.pack('<h', int(8000 * math.sin(2 * math.pi * frequency * i / rate)))
                for i in range(int(rate * seconds))
            )
        )


def step(description, seconds):
    print(f'\n{description}')
    time.sleep(seconds)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', action='store_true', help='also play an mp3 from a URL')
    args = parser.parse_args()

    tmp = tempfile.mkdtemp()
    low = os.path.join(tmp, 'low.wav')
    high = os.path.join(tmp, 'high.wav')
    write_tone(low, 330, 2)
    write_tone(high, 660, 1)

    sound = Sound(low)  # noqa: F405

    print('Expect: a low tone for 2 seconds.')
    sound.play()
    step('Expect: silence for 1 second (the tone finished).', 3)

    print('Expect: the low tone for 1 second, then it pauses.')
    sound.play(restart=True)
    time.sleep(1)
    sound.pause()
    step('Expect: silence for 1 second (paused).', 1)
    print('Expect: the rest of the low tone, about 1 second (resumed).')
    sound.play()
    time.sleep(1.5)

    print('\nExpect: the low tone, restarting from the beginning twice.')
    sound.play()
    time.sleep(0.7)
    sound.play(restart=True)
    time.sleep(0.7)
    sound.play(restart=True)
    time.sleep(2.2)

    print('\nExpect: the low tone at about a quarter volume.')
    sound.setVolume(0.25)
    sound.play()
    time.sleep(2.2)
    print(f'getVolume() returned {sound.getVolume()} (expected 0.25)')
    sound.setVolume(1.0)

    # The bug this checks: dropping a Sound used to stop it immediately
    print('\nExpect: a high tone for 1 second, from a Sound that is')
    print('garbage-collected right after play() -- Sound(url).play().')
    Sound(high).play()  # noqa: F405
    import gc

    gc.collect()
    time.sleep(1.5)

    print('\nExpect: the high tone looping for about 3 seconds, from a')
    print('garbage-collected Sound, until this script exits.')
    Sound(high).play(loop=True)  # noqa: F405
    gc.collect()
    time.sleep(3)

    if args.url:
        print('\nExpect: a march, downloaded from a URL, for 4 seconds.')
        march = Sound(MP3_URL)  # noqa: F405
        march.play()
        time.sleep(4)

    print('\nDone.')
    # Skip cmu_graphics' exit handlers, since no app was run
    os._exit(0)


if __name__ == '__main__':
    main()
