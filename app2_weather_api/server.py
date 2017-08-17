from flask import Flask, request, render_template
from random import choice, randint
import urllib2
import json
from secrets import *

from pprint import pprint

app = Flask(__name__)

RAIN_WORDS = ['rain', 'storm', 'sleet']

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/result')
# def result():
#     if forecastday=='rain':
#         return render_template("rainny.html")
#     else:
#         return render_template("notrainny.html")


@app.route('/getlocation')
def get_location():
    #Get location, pass it to the API
    zip = request.args.get("zip").replace(' ','')
    city = request.args.get("city").replace(' ','_')
    state = request.args.get("state").replace(' ','')
    url_part1 = 'http://api.wunderground.com/api/' + API_KEY + '/forecast/geolookup/conditions/q/'
    url_lastpart = '.json'
    if zip == 'rain':
        forecasticon_url = '/static/rain.jpg'
        return render_template("rainny.html", location='', icon=forecasticon_url, temp='', day='')
    elif state and city:
        f = urllib2.urlopen(url_part1 + state + '/' + city + url_lastpart)
    elif zip:
        f = urllib2.urlopen(url_part1 + zip + url_lastpart)
    else:
        errortext = "Please enter either a zipcode ~OR~ state and city"
        return render_template("error.html", errortext=errortext)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    if 'error' in parsed_json['response']:
        errortext = parsed_json['response']['error']['description']
        return render_template("error.html", errortext=errortext)
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    location = city + ", " + state
    temp_f = parsed_json['current_observation']['temp_f']
    forecastday = parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon']
    forecasttext = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
    chanceofrain = parsed_json['forecast']['txt_forecast']['forecastday'][0]['pop']
    forecasticon_url = parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon_url']
    day = parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
    f.close()
    # check if our rain-words are in the icon name (forecastday)
    if any(x in forecastday for x in RAIN_WORDS):
        return render_template("rainny.html", location=location, icon=forecasticon_url,
                               temp=temp_f, day=day, fctext=forecasttext, pop=chanceofrain)
    else:
        return render_template("notrainny.html", location=location, icon=forecasticon_url,
                               temp=temp_f, day=day, fctext=forecasttext, pop=chanceofrain)


if __name__ == "__main__":
    app.run(debug=True)
