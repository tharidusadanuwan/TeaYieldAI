import os
import requests

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv(
    "OPENWEATHER_API_KEY"
)



def get_weather(location):


    url="https://api.openweathermap.org/data/2.5/weather"



    params={

        "q":location,

        "appid":API_KEY,

        "units":"metric"

    }



    response=requests.get(
        url,
        params=params
    )



    data=response.json()



    if response.status_code != 200:

        raise Exception(data)



    return {


        "temperature":
        data["main"]["temp"],


        "humidity":
        data["main"]["humidity"],


        "wind_speed":
        data["wind"]["speed"],


        "weather_condition":
        data["weather"][0]["description"],


        "rainfall":
        data.get("rain",{}).get("1h",0)

    }