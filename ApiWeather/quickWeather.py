#! python3
# quickWeather.py -- Wyświetla prognozę pogody dla lokalizacji podanej w wierszu poleceń.

import json, requests, sys

# Ustalenie lokalizacji na podstawie argumentów wiersza poleceń.

"""if len(sys.argv) < 2:
    print('Użycie: quickWeather.py lokalizacja')
    sys.exit()
"""
#location = ' '.join(sys.argv[1:])
apiKey = "d97065256f27595d6304715ddd704dea"
location = "Gdansk,pl"
# Pobieranie danych w formacie JSON z API witryny OpenWeatherMap.org
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (location, apiKey)
print(url)
response = requests.get(url)
response.raise_for_status()

# Umieszczenie danych JSON w zmiennej Pythona.
weatherData = json.loads(response.text)

# Wyświetlenie opisu prognozy pogody.
w = weatherData

print("Today in %s:" % (location))
print()

def kelwinToCelsiusKonwerter(kelwin):
    celsius = kelwin - 273.15
    return round(celsius,2)

actualTemp = kelwinToCelsiusKonwerter(w['main']['temp'])
feelsLikeTemp = kelwinToCelsiusKonwerter(w['main']['feels_like'])
minTemp = kelwinToCelsiusKonwerter(w['main']['temp_min'])
maxTemp = kelwinToCelsiusKonwerter(w['main']['temp_max'])

print('Actual weather in %s:' % (location))
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])
print("Actual temperature:     %s °C\nfeels like temperature: %s °C" % (actualTemp, feelsLikeTemp))
print("Minimal temperature:    %s °C\nMaksimal temperature:   %s °C" % (minTemp, maxTemp))

