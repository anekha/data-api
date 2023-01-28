# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    # YOUR CODE HERE
    url = BASE_URI + '/geo/1.0/direct?q=' + query + '&limit=5'
    response = requests.get(url).json()
    if response == []:
        print("City does not exist")
        return None
    if len(response) == 1:
        return response[0]
    else:
        country_list = list(enumerate(response))
        for country in country_list:
            print(str((country[0] + 1)) + '. ' + country[1]['name'] + "," + country[1]['country'])
        print('Multiple matches found, which city did you mean?')
        city_index = int(input("Index?\n> ")) - 1
        return response[city_index]





def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    # YOUR CODE HERE
    url_weather = 'https://weather.lewagon.com/data/2.5/forecast?lat='+ str(lat) + '&lon=' + str(lon) + '&units=metric'
    response_weather = requests.get(url_weather).json()
    #print(url_weather)
    return response_weather['list'][0:5]


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city
    # YOUR CODE HERE
    lat = city['lat']
    lon = city['lon']
    fived_weather_forecast = weather_forecast(lat, lon)
    for x in fived_weather_forecast:
        print(x['dt_txt'],x['weather'][0]['description'],x['main']['temp'])

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
