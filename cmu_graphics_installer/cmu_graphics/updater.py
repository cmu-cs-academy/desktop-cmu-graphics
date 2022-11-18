from datetime import datetime
import json
import math
import os
import sys
import json

CMU_GRAPHICS_NO_UPDATE = True
FORCE_UPDATE = os.environ.get('CMU_GRAPHICS_AUTO_UPDATE') is not None

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.insert(0, parent_directory)
update_config_file_path = os.path.join(current_directory, 'meta/updates.json')

def update():
    import shutil
    import zipfile
    from libs import webrequest

    zip_bytes = webrequest.get(
        'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/cmu_graphics_installer.zip'
    ).read()
    zip_path = os.path.join(parent_directory, 'cmu_graphics_installer.zip')
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with open(zip_path, 'xb') as f:
        f.write(zip_bytes)

    installer_dir = os.path.join(parent_directory, 'cmu_graphics_installer')
    if os.path.exists(installer_dir):
        shutil.rmtree(installer_dir)
    os.mkdir(installer_dir)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(parent_directory)
    os.remove(zip_path)

def get_update_info():
    if os.path.exists(update_config_file_path):
        with open(update_config_file_path, 'r') as f:
            return json.loads(f.read())
    return {}

def save_update_info(update_info):
    with open(update_config_file_path, 'w') as f:
        f.write(json.dumps(update_info))

def skipUpdate():
    update_info= get_update_info()
    update_info['skip_past'] = most_recent_version
    save_update_info(update_info)

def updateLater():
    update_info= get_update_info()
    update_info['last_attempt'] = datetime.now().timestamp()
    save_update_info(update_info)

def onMouseMove(mouseX, mouseY):
    if app.mode != 'selection':
        return

    for button in [app.downloadNow, app.downloadLater, app.skipThisVersion]:
        if button.hits(mouseX, mouseY):
            button.fill=rgb(128, 179, 191)
        else:
            button.fill = rgb(90,153,179)

def startUpdate():
    app.group.clear()
    app.updateIn = 10
    Label('Updating ...', 200, 200, size=30)
    app.mode = 'update'

def onMousePress(mouseX, mouseY):
    if app.mode != 'selection':
        return

    if app.downloadNow.hits(mouseX, mouseY):
        startUpdate()
    elif app.downloadLater.hits(mouseX, mouseY):
        # No action here because we "update later" on every run
        # No matter the outcome, don't check again until tomorrow
        app.quit()
    elif app.skipThisVersion.hits(mouseX, mouseY):
        skipUpdate()
        app.quit()

def makeFirework():
    fireWorkColors = [ 'red', 'lime', 'magenta', 'yellow', 'orangeRed',
                       'powderBlue' ]
    randomColor = fireWorkColors[randrange(0, len(fireWorkColors))]
    x, y = randrange(0, 400), randrange(0, 100)

    # Makes the firework.
    newStream = Line(x, 400, x, 460, fill=randomColor)
    newStream.fireworkHeight = y
    newStream.color = randomColor
    streams.add(newStream)

def makeNewExplosion(cx, cy, color):
    # Firework goes off.
    firework = Group(
        Star(cx, cy, randrange(5, 20), 100, fill=color),
        Star(cx, cy, 1, 30, fill=color, roundness=10)
        )
    fireworks.add(firework)

def animateLaunches():
    # Moves the firework trails up.
    streams.toFront()
    for stream in streams.children:
        stream.top -= 5
        stream.opacity -= 1

        # If the firework has reached the height, it should explode.
        if (stream.top <= stream.fireworkHeight):
            streams.remove(stream)
            makeNewExplosion(stream.x1, stream.y1, stream.color)

def animateExplosions():
    # Expands and fades out all of the explosions.
    fireworks.toFront()
    for firework in fireworks.children:
        firework.width += 1
        firework.height += 1
        firework.opacity -= 2
        firework.rotateAngle += 5

        # Once the firework has faded enough, removes it completely.
        if (firework.opacity <= 3):
            fireworks.remove(firework)

def onStep():
    animateExplosions()
    animateLaunches()
    if (app.timeToNextFirework <= 0  and app.totalFireworks < 6):
        makeFirework()
        app.totalFireworks += 1
        app.timeToNextFirework = 10
    app.timeToNextFirework -= 1
    app.updateIn -= 1

    if app.updateIn == 0:
        update()
        sys.exit()

def drawSelectionScreen(most_recent_version):
    Label(
        "Version %s of CMU Graphics" % most_recent_version,
        200, 25,
        size = 25
    )
    Label(
        "is available for download",
        200, 60,
        size = 25
    )

    app.downloadNow = Rect(50, 90, 300, 75, fill=rgb(90,153,179))
    Label("Update Now", 200, 90 + (75 / 2), align='center', fill='white', size=25)
    app.downloadLater = Rect(50, 190, 300, 75, fill=rgb(90,153,179))
    Label("Update Later", 200, 190 + (75 / 2), align='center', fill='white', size=25)
    app.skipThisVersion = Rect(50, 290, 300, 75, fill=rgb(90,153,179))
    Label("Skip This Version", 200, 290 + (75 / 2), align='center', fill='white', size=25)

def drawCompletionScreen():
    Label('Done!', 200, 175, size=30)
    Label('Rerun your app to continue', 200, 225, size=30)

if __name__ == '__main__':
    command = json.loads(input())

    from cmu_graphics import *

    fireworks = Group()
    streams = Group()
    app.totalFireworks = 0
    app.timeToNextFirework = 0
    app.updateIn = math.inf

    if command['type'] == 'request_update':
        updateLater()
        app.mode = 'selection'
        drawSelectionScreen(command['most_recent_version'])
        if FORCE_UPDATE:
            startUpdate()
    elif command['type'] == 'complete_update':
        app.mode = 'complete'
        drawCompletionScreen()
        if FORCE_UPDATE:
            sys.exit()

    cmu_graphics.loop()
