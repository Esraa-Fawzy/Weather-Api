import requests
import json
from flask import request, Flask,jsonify


app = Flask(__name__)


@app.route("/weather/", methods=['GET'])
def current_weather():
    #get country name from url parameter
    countryname = request.args.get('country', default=None, type=str)

    url = 'http://api.openweathermap.org/data/2.5/weather?'
    key = 'f54190c2447594d9b39e44d0d4b31214'

    if countryname:

        params={
            "q":countryname,
            "APPID": key
        }
        res = requests.get(url, params=params)
        
        res= json.loads(res.text)
        weather = res['weather'][0]['description']
        temp_max=res['main']['temp_max']
        temp_min = res['main']['temp_min']
        humidtiy=res['main']['humidity']

        response = "<h2>The weather of {} is {},maximum tempreture is {},minmum tempreture is {} and it's humidity {}</h2>".format(
        countryname, weather, temp_max, temp_min, humidtiy)

 
    else:
        response = "<h1>Not found :(</h1>"

    return response


@app.route('/')
def index():
    return ('<h1>All is working !</h1>')


if __name__ == "__main__":
    app.run(debug=True)
