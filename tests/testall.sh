set -ex

export SDL_VIDEODRIVER=dummy

python3 test_image_gen.py
python3 test_get_text_input.py
python3 test_autoupdate.py
