import sys
from cmu_graphics import *

# The APIs we are using, from Open-Meteo (https://open-meteo.com). They are
# free for non-commercial use and don't need an API key.
GEOCODING_API = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_API = 'https://api.open-meteo.com/v1/forecast'

# Open-Meteo describes the weather with a number, called a WMO weather code.
# This maps each code to a description, and to the kind of icon we draw for it.
WEATHER_CODES = {
    0: ('Clear', 'clear'),
    1: ('Mostly Clear', 'partlyCloudy'),
    2: ('Partly Cloudy', 'partlyCloudy'),
    3: ('Overcast', 'cloudy'),
    45: ('Fog', 'fog'),
    48: ('Fog', 'fog'),
    51: ('Light Drizzle', 'rain'),
    53: ('Drizzle', 'rain'),
    55: ('Heavy Drizzle', 'rain'),
    56: ('Freezing Drizzle', 'rain'),
    57: ('Freezing Drizzle', 'rain'),
    61: ('Light Rain', 'rain'),
    63: ('Rain', 'rain'),
    65: ('Heavy Rain', 'rain'),
    66: ('Freezing Rain', 'rain'),
    67: ('Freezing Rain', 'rain'),
    71: ('Light Snow', 'snow'),
    73: ('Snow', 'snow'),
    75: ('Heavy Snow', 'snow'),
    77: ('Snow Grains', 'snow'),
    80: ('Rain Showers', 'rain'),
    81: ('Rain Showers', 'rain'),
    82: ('Heavy Showers', 'rain'),
    85: ('Snow Showers', 'snow'),
    86: ('Snow Showers', 'snow'),
    95: ('Thunderstorm', 'storm'),
    96: ('Thunderstorm', 'storm'),
    99: ('Thunderstorm', 'storm'),
}

# Given a name of a city, this function returns information about the weather
# in that city, and information about the city itself. If no city has that
# name, it returns None, None instead.
def getAPIData(city):
    # First, look up the city by name to find where it is. requests adds the
    # params to the URL for us, including turning characters like spaces into
    # a form that's allowed in a URL. The timeout (in seconds) stops the app
    # from waiting forever if the server doesn't answer.
    cityResults = requests.get(
        GEOCODING_API, params={'name': city, 'count': 1}, timeout=10
    ).json()
    if 'results' not in cityResults:
        return None, None
    cityData = cityResults['results'][0]

    # Then ask for the current weather at the city's latitude and longitude
    weatherData = requests.get(
        WEATHER_API,
        params={
            'latitude': cityData['latitude'],
            'longitude': cityData['longitude'],
            'current': 'temperature_2m,weather_code,wind_direction_10m,is_day',
            'temperature_unit': 'fahrenheit',
        },
        timeout=10,
    ).json()['current']

    return weatherData, cityData

# Turns a wind direction in degrees (0 is north, 90 is east) into a compass
# direction like 'NE'
def compassDirection(degrees):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return directions[pythonRound(degrees / 45) % 8]

# The weather icons are drawn with shapes, centered on (cx, cy)
def drawSun(cx, cy):
    for angle in range(0, 360, 45):
        x1, y1 = getPointInDir(cx, cy, angle, 45)
        x2, y2 = getPointInDir(cx, cy, angle, 65)
        Line(x1, y1, x2, y2, fill='orange', lineWidth=6)
    Circle(cx, cy, 35, fill='gold')

def drawMoon(cx, cy):
    Circle(cx, cy, 45, fill='gold')
    # Cover part of the moon with a circle the color of the background, so
    # what's left is a crescent
    Circle(cx + 22, cy - 15, 40, fill='white')

def drawCloud(cx, cy, color):
    Circle(cx - 35, cy + 5, 28, fill=color)
    Circle(cx, cy - 15, 38, fill=color)
    Circle(cx + 35, cy + 5, 28, fill=color)
    Rect(cx - 35, cy + 5, 70, 28, fill=color)

def drawWeatherIcon(kind, isDay, cx, cy):
    if kind == 'clear':
        if isDay:
            drawSun(cx, cy)
        else:
            drawMoon(cx, cy)
    elif kind == 'partlyCloudy':
        if isDay:
            # Lower than the moon, so its rays stay clear of the description
            drawSun(cx - 30, cy - 15)
        else:
            drawMoon(cx - 30, cy - 30)
        drawCloud(cx + 15, cy + 15, 'lightGray')
    elif kind == 'cloudy':
        drawCloud(cx, cy, 'darkGray')
    elif kind == 'fog':
        for i in range(4):
            y = cy - 35 + i * 25
            Line(cx - 60, y, cx + 60, y, fill='darkGray', lineWidth=12)
    elif kind == 'rain':
        drawCloud(cx, cy - 20, 'darkGray')
        for x in range(-40, 41, 20):
            Line(cx + x, cy + 25, cx + x - 10, cy + 55, fill='blue', lineWidth=4)
    elif kind == 'snow':
        drawCloud(cx, cy - 20, 'lightGray')
        for x in range(-40, 41, 20):
            Star(cx + x, cy + 45, 10, 6, fill='deepSkyBlue', roundness=40)
    elif kind == 'storm':
        drawCloud(cx, cy - 20, 'dimGray')
        Polygon(cx + 5, cy + 5, cx - 20, cy + 45, cx, cy + 45, cx - 10, cy + 75,
                cx + 25, cy + 30, cx + 5, cy + 30, cx + 15, cy + 5, fill='gold')

# Given a city, queries Open-Meteo to find its weather information,
# then draws that weather to the canvas
def drawWeather(city):
    app.group.clear()

    weatherData, cityData = getAPIData(city)
    if cityData is None:
        drawSearchPage()
        Label('City not found. Try another!', 200, 250, size=20)
        return

    # Draws the title "Weather in City: Rainy"
    Label('Weather in ', 200, 30, size=40)
    Label(cityData['name'], 200, 75, size=40 if len(cityData['name']) < 15 else 25)
    description, iconKind = WEATHER_CODES.get(
        weatherData['weather_code'], ('Unknown', 'cloudy')
    )
    Label(description, 200, 130, size=30)

    drawWeatherIcon(iconKind, weatherData['is_day'] == 1, 200, 230)

    # Draws the temperature in Farenheit and the wind direction
    Label(str(pythonRound(weatherData['temperature_2m'])) + '°F',
          25, 350, align='left', size=30)
    Label('Wind: ' + compassDirection(weatherData['wind_direction_10m']),
          375, 350, align='right', size=30)

    # Open-Meteo asks that apps using its data say where it came from
    Label('Weather data by Open-Meteo.com', 200, 390, size=10, fill='gray')

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

# Search for a city when we press the s key, and try to draw its weather.
# If we can't reach Open-Meteo, show an error message.
def onKeyPress(key):
    # Without requests, there's no way to search
    if not app.hasRequests:
        return
    if key.lower() == 's':
        city = app.getTextInput('City Name:')
        if not city:
            return
        try:
            drawWeather(city)
        except Exception:
            app.group.clear()
            drawSearchPage()
            Label("Couldn't get the weather.", 200, 250, size=20)
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

# Try to load the necessary third party libraries, create our back button, and
# start the application. If loading the libraries fails, print a message about
# installation
def start():
    # The visibility of the back button changes when we draw the weather,
    # and it is accessed in the mouse press handler, so it needs to be
    # part of the app
    app.backButton = Group(
        Line(30, 30, 80, 30, lineWidth=10),
        RegularPolygon(30, 30, 15, 3, rotateAngle=-90),
        visible=False
    )

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
