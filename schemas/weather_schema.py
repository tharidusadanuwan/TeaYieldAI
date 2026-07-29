from pydantic import BaseModel

from datetime import datetime





class WeatherBase(BaseModel):


    field_id:int


    temperature:float | None = None


    humidity:float | None = None


    rainfall:float | None = None


    wind_speed:float | None = None


    weather_condition:str | None = None







class WeatherCreate(WeatherBase):

    pass







class WeatherUpdate(BaseModel):


    temperature:float | None = None


    humidity:float | None = None


    rainfall:float | None = None


    wind_speed:float | None = None


    weather_condition:str | None = None







class WeatherResponse(WeatherBase):


    weather_id:int


    recorded_date:datetime



    class Config:

        from_attributes = True