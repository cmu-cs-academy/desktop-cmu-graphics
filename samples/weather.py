import sys
from cmu_graphics import *

API_BASE = 'https://www.metaweather.com'

app.backButton = None

def celciusToFarenheit(degrees):
    return ((degrees / 5) * 9) + 32

def getAPIData(city):
    cityData = requests.get(
        API_BASE + '/api/location/search/?query=' + city
    ).json()[0]
    cityWoeid = cityData['woeid']
    weatherData = requests.get(
        API_BASE + '/api/location/' + str(cityWoeid) + '/'
    ).json()['consolidated_weather'][0]

    return weatherData, cityData

def drawWeather(city):
    weatherData, cityData = getAPIData(city)

    app.group.clear()
    Label('Weather in ', 200, 30, size=40)
    Label(cityData['title'], 200, 75, size=40)
    Label(weatherData['weather_state_name'], 200, 130, size=30)
    weather_state = weatherData['weather_state_abbr']
    imageURL = API_BASE + '/static/img/weather/png/'+ weather_state + '.png'
    Image(imageURL, 200, 230, align='center', width=150, height=150)

    farenheitTemp = celciusToFarenheit(weatherData['the_temp'])
    Label(str(pythonRound(farenheitTemp, 2)) + '°F',
          25, 350, align='left', size=30)
    Label('Wind: ' + weatherData['wind_direction_compass'],
          375, 350, align='right', size=30)

    app.backButton = Line(80, 30, 20, 30, arrowEnd=True, lineWidth=5)

def onMousePress(mouseX, mouseY):
    if app.backButton is not None and app.backButton.hits(mouseX, mouseY):
        app.group.clear()
        app.backButton = None
        drawSearchPage()

def drawSearchPage():
    Label('Press S to search for a city.', 200, 200, size=25)

def onKeyPress(key):
    if key.lower() == 's':
        city = app.getTextInput('City Name:')
        try:
            drawWeather(city)
        except:
            Label('City not found. Try another!', 200, 250, size=20)

def drawText(linesList):
    lineHeight = 30
    lineX = 200 - ((len(linesList) * lineHeight) // 2)
    for line in linesList:
        Label(line, 200, lineX, align='center', size=20)
        lineX += lineHeight

def loadModules():
    import requests
    globals()['requests'] = requests

def start():
    try:
        loadModules()
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

cmu_graphics.loop()
