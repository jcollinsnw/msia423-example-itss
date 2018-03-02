from flask import render_template, request, redirect, url_for, flash
from msiapp import application, db
from msiapp.models import Track, City
import requests
import json
import os
import time

@application.route('/')
def index():
    """Main view that lists songs

    Create view into index page that uses data queried from Track database and
    inserts it into the msiapp/templates/index.html template

    :return: rendered html template

    """

    return render_template('index.html', tracks=Track.query.all())

@application.route('/add', methods=['POST'])
def add_entry():
    """View that process a POST with new song input

    :return: redirect to index page
    """

    track1 = Track(artist=request.form['artist'], album=request.form['album'], title=request.form['title'])
    db.session.add(track1)
    db.session.commit()

    return redirect(url_for('index'))

@application.route('/city')
def city():
    return render_template('city.html', cities = City.query.all())

@application.route('/addCity', methods=['POST'])
def add_city():
    """View that process a POST with new song input

    :return: redirect to index page
    """
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (
                request.form['city'],
                os.environ['MAPS_KEY'])

    response = requests.get(url)

    # debug
    weather = json.loads(response.text)
    timestamp = int(time.time())
    name = weather['name']
    country = weather['sys']['country']
    temperature = weather['main']['temp']
    max_temp = weather['main']['temp_max']
    min_temp = weather['main']['temp_min']
    city = City(name=name,timestamp=timestamp,country=country,temperature=temperature,max_temp=max_temp,min_temp=min_temp)
    db.session.add(city)
    db.session.commit()

    return redirect(url_for('city'))

if __name__ == "__main__":
    application.run(debug=True)
