from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from database import get_db


from models.weather import WeatherData


from schemas.weather_schema import (

    WeatherCreate,

    WeatherUpdate,

    WeatherResponse

)




router = APIRouter(

    prefix="/api/weather",

    tags=["Weather"]

)







# GET ALL WEATHER

@router.get(

    "/",

    response_model=list[WeatherResponse]

)

def get_weather(

    db:Session = Depends(get_db)

):


    return db.query(

        WeatherData

    ).all()





@router.get(
    "/field/{field_id}/date/{weather_date}"
)
def get_weather_by_date(

    field_id:int,

    weather_date:str,

    db:Session=Depends(get_db)

):


    print(
        "FIELD:",
        field_id
    )


    print(
        "DATE:",
        weather_date
    )


    weather = db.query(
        WeatherData
    ).filter(

        WeatherData.field_id == field_id

    ).all()



    print(
        "FOUND:",
        weather
    )



    for item in weather:

        if str(item.recorded_date.date()) == weather_date:

            return item



    raise HTTPException(

        status_code=404,

        detail="Weather data not found"

    )



# GET SINGLE WEATHER


@router.get(

    "/{weather_id}",

    response_model=WeatherResponse

)

def get_single_weather(

    weather_id:int,

    db:Session = Depends(get_db)

):


    weather = db.query(

        WeatherData

    ).filter(

        WeatherData.weather_id == weather_id

    ).first()



    if not weather:


        raise HTTPException(

            status_code=404,

            detail="Weather not found"

        )


    return weather







# CREATE WEATHER


@router.post(

    "/",

    response_model=WeatherResponse

)

def create_weather(

    weather:WeatherCreate,

    db:Session = Depends(get_db)

):


    new_weather = WeatherData(

        **weather.dict()

    )



    db.add(

        new_weather

    )


    db.commit()


    db.refresh(

        new_weather

    )


    return new_weather







# UPDATE WEATHER


@router.put(

    "/{weather_id}",

    response_model=WeatherResponse

)

def update_weather(

    weather_id:int,

    weather:WeatherUpdate,

    db:Session = Depends(get_db)

):


    existing = db.query(

        WeatherData

    ).filter(

        WeatherData.weather_id == weather_id

    ).first()



    if not existing:


        raise HTTPException(

            status_code=404,

            detail="Weather not found"

        )




    update_data = weather.dict(

        exclude_unset=True

    )



    for key,value in update_data.items():


        setattr(

            existing,

            key,

            value

        )




    db.commit()


    db.refresh(

        existing

    )


    return existing







# DELETE WEATHER


@router.delete(

    "/{weather_id}"

)

def delete_weather(

    weather_id:int,

    db:Session = Depends(get_db)

):


    weather = db.query(

        WeatherData

    ).filter(

        WeatherData.weather_id == weather_id

    ).first()



    if not weather:


        raise HTTPException(

            status_code=404,

            detail="Weather not found"

        )



    db.delete(

        weather

    )


    db.commit()



    return {


        "message":

        "Weather deleted successfully"


    }