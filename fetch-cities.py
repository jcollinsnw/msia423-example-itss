from msiapp import db
from msiapp.models import City

import requests
import os
import json
import time

<<<<<<< HEAD
API_KEY = os.environ['MAPS_KEY']

=======
# get the key by creating an account in openweathermap and generating an app key. 
# set this key in your AWS Elastic Beanstalk Environment
API_KEY = os.environ['OPENWEATHERMAP_KEY']
>>>>>>> 1603318... removed key

def get_weather_for_city(city):
        url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (
                city,
                API_KEY)

        response = requests.get(url)

        # debug
        print(response.text)
        return json.loads(response.text)



def ingest_cities():
        cities = ['Lisbon']
        for city in cities:
                weather = get_weather_for_city(city)

                # json parsing below
                timestamp = int(time.time())
                name = weather['name']
                country = weather['sys']['country']
                temperature = weather['main']['temp']
                max_temp = weather['main']['temp_max']
                min_temp = weather['main']['temp_min']

                print(name)
                print(timestamp)
                print(country)
                print(temperature)
                print(max_temp)
                print(min_temp)

                # STORE in RDS
                city = City(name=name,timestamp=timestamp,country=country,temperature=temperature,max_temp=max_temp,min_temp=min_temp)
                db.session.add(city)
                db.session.commit()
                print("stored [%s]" % name)


if __name__ == "__main__":
        ingest_cities()
