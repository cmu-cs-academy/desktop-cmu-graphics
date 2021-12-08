import sys
from cmu_graphics import *

# The base URL for the API we are using: metaweather
API_BASE = 'https://www.metaweather.com'

def celciusToFarenheit(degrees):
    return ((degrees / 5) * 9) + 32

# Given a name of a city, this function returns information about the weather
# in that city, and information about the city itself
def getAPIData(city):
    # First query the API to get information about the city given its name
    cityData = requests.get(
        API_BASE + '/api/location/search/?query=' + city
    ).json()[0]

    # Extract the Where On Earth Identifier from the city information
    cityWoeid = cityData['woeid']

    # Then query the API using the woeid to get its weather
    weatherData = requests.get(
        API_BASE + '/api/location/' + str(cityWoeid) + '/'
    ).json()['consolidated_weather'][0]

    return weatherData, cityData

# Given a city, queries the metaweather API to find its weather information,
# then draws that weather to the canvas
def drawWeather(city):
    app.group.clear()

    weatherData, cityData = getAPIData(city)

    # Draws the title "Weather in City: Rainy"
    Label('Weather in ', 200, 30, size=40)
    Label(cityData['title'], 200, 75, size=40)
    Label(weatherData['weather_state_name'], 200, 130, size=30)

    # Given the weather state (sunny, cloudy, windy, etc)
    # Get an image from metawetaher representing that weather state
    weather_state = weatherData['weather_state_abbr']
    imageURL = API_BASE + '/static/img/weather/png/'+ weather_state + '.png'
    Image(imageURL, 200, 230, align='center', width=150, height=150)

    # Draws the temperature in Farenheit and the wind direction
    # The temperature returned from metaweather is in Celcius, so we have
    # to convert it first
    farenheitTemp = celciusToFarenheit(weatherData['the_temp'])
    Label(str(pythonRound(farenheitTemp, 2)) + '°F',
          25, 350, align='left', size=30)
    Label('Wind: ' + weatherData['wind_direction_compass'],
          375, 350, align='right', size=30)

    # Make the back button visible so we can return to the search page
    app.backButton.visible = True

def onMousePress(mouseX, mouseY):
    # If the back button is visible (which means we're displaying the weather
    # for a city right now), and we click it, go back to the search page
    if app.backButton.visible and app.backButton.hits(mouseX, mouseY):
        app.backButton.visible = False
        app.group.clear()
        drawSearchPage()

def drawSearchPage():
    Label('Press S to search for a city.', 200, 200, size=25)

# Search for a city when we press the s key, and try to draw its weather
# If we can't find the city, print an error message
def onKeyPress(key):
    if key.lower() == 's':
        city = app.getTextInput('City Name:')
        try:
            drawWeather(city)
        except:
            Label('City not found. Try another!', 200, 250, size=20)

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

# Try to load the necessary third party libraries, create our back button, and
# start the application. If loading the libraries fails, print a message about
# installation
def start():
    try:
        loadModules()
        # The visibility of the back button changes when we draw the weather,
        # and it is accessed in the mouse press handler, so it needs to be
        # part of the app
        app.backButton = Group(
            Line(30, 30, 80, 30, lineWidth=10),
            RegularPolygon(30, 30, 15, 3, rotateAngle=-90),
            visible=False
        )
        drawSearchPage()
    except:
        drawText([
            'This program requires "requests".',
            'This is third party library which can',
            'be installed by running the command',
            'printed to the console in the application',
            '"Command Prompt".' if sys.platform == 'win32' else '"Terminal".',
        ])
        if sys.platform == 'win32':
            print('"%s" -m pip install requests' % sys.executable)
        else:
            print('sudo "%s" -m pip install requests' % sys.executable)
        app.mode = 'helpText'

start()

cmu_graphics.run()
