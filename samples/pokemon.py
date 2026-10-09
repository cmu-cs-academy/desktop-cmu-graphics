import sys
from cmu_graphics import *

# The API we are using, PokeAPI (https://pokeapi.co). It is free and doesn't
# need an API key. We add the name of a Pokémon to the end of this URL.
POKEMON_API = 'https://pokeapi.co/api/v2/pokemon/'

# Given the name of a Pokémon, asks PokeAPI about it and draws what we learn
# to the canvas
def drawPokemon(name):
    app.group.clear()
    app.cryButton = None

    # The timeout (in seconds) stops the app from waiting forever if the
    # server doesn't answer
    response = requests.get(POKEMON_API + name, timeout=10)

    # A status code of 200 means everything went well. PokeAPI answers with
    # 404 when no Pokémon has that name.
    if response.status_code != 200:
        drawSearchPage()
        Label('Pokémon not found. Try another!', 200, 250, size=20)
        return

    # Turn the response into Python dictionaries and lists
    data = response.json()

    Label(data['name'].capitalize(), 200, 35, size=40)

    # Images can come straight from a URL. Setting width and height scales
    # the picture to fit.
    imageURL = data['sprites']['other']['official-artwork']['front_default']
    Image(imageURL, 200, 165, align='center', width=200, height=200)

    # A Pokémon has one or two types, so we join all of them together
    types = ''
    for typeInfo in data['types']:
        if types != '':
            types += ' / '
        types += typeInfo['type']['name']

    # PokeAPI gives height in decimeters and weight in hectograms, so we
    # divide by 10 to get meters and kilograms
    height = data['height'] / 10
    weight = data['weight'] / 10
    Label('Type: ' + types + '   Height: ' + str(height) + ' m' +
          '   Weight: ' + str(weight) + ' kg', 200, 290, size=16)

    # Some Pokémon don't have a cry, so we only draw the button if one exists
    cryURL = data['cries']['latest']
    if cryURL != None:
        app.cry = Sound(cryURL)
        app.cryButton = Rect(140, 320, 120, 40, fill='gold', border='black')
        Label('Play cry', 200, 340, size=18)

    Label('Press S to search', 200, 385, size=12, fill='gray')

def onMousePress(mouseX, mouseY):
    # If there's a cry button on the screen and we click it, play the cry
    if app.cryButton != None and app.cryButton.hits(mouseX, mouseY):
        app.cry.play(restart=True)

def drawSearchPage():
    Label('Press S to search for a Pokémon.', 200, 200, size=22)

# Search for a Pokémon when we press the s key, and try to draw it.
# If we can't reach PokeAPI, show an error message.
def onKeyPress(key):
    # Without requests, there's no way to search
    if not app.hasRequests:
        return
    if key.lower() == 's':
        name = app.getTextInput('Pokémon Name:')
        if not name:
            return
        try:
            drawPokemon(name.lower().strip())
        except Exception:
            app.group.clear()
            app.cryButton = None
            drawSearchPage()
            Label("Couldn't reach PokeAPI.", 200, 250, size=20)
            Label('Check your internet connection.', 200, 280, size=20)

# A helper function for drawing text centered on the screen
def drawText(linesList):
    lineHeight = 30
    # lineY starts out at the center (200) minus half the height of our
    # whole block of text
    lineY = 200 - ((len(linesList) * lineHeight) // 2)
    for line in linesList:
        # Create a label for each line, and move lineY down so the next
        # line is drawn lower
        Label(line, 200, lineY, align='center', size=20)
        lineY += lineHeight

# This function loads the third party library requests, and adds
# it to the global namespace so we can use it in other functions.
def loadModules():
    global requests
    import requests

# Prints how to install requests, set off from the rest of the console output
# so it's easy to find. The command uses the Python that's running this
# program, so requests gets installed where this program will find it.
def printInstallInstructions():
    if sys.platform == 'win32':
        terminalName = 'Command Prompt'
    else:
        terminalName = 'Terminal'
    print()
    print('=' * 70)
    print('This program needs the "requests" library, which isn\'t installed.')
    print()
    print('To install it, open ' + terminalName + ', paste in this command,')
    print('and press Enter:')
    print()
    print('    "%s" -m pip install requests' % sys.executable)
    print()
    print('Then run this program again.')
    print('=' * 70)
    print()

# Try to load the necessary third party libraries and start the application.
# If loading the libraries fails, print a message about installation
def start():
    # The cry button is drawn when we show a Pokémon, and it is checked in
    # the mouse press handler, so it needs to be part of the app
    app.cryButton = None

    try:
        loadModules()
        app.hasRequests = True
    except ImportError:
        app.hasRequests = False
        drawText([
            'This program requires "requests".',
            'This is a third party library which',
            'can be installed by running the',
            'command printed to the console in',
            'the application "Command Prompt".'
            if sys.platform == 'win32'
            else 'the application "Terminal".',
        ])
        printInstallInstructions()
        return

    drawSearchPage()

start()

cmu_graphics.run()
