from datetime import date

from apscheduler.schedulers.background import BackgroundScheduler

from database import SessionLocal

from models.weather import WeatherData

from models.tea_field import TeaField

from services.weather_service import get_weather



scheduler = BackgroundScheduler()





def fetch_all_weather():


    db = SessionLocal()



    try:


        today = date.today()



        fields = db.query(
            TeaField
        ).all()





        for field in fields:



            if not field.location:

                continue





            # CHECK TODAY WEATHER EXISTS

            existing_weather = db.query(
                WeatherData
            ).filter(

                WeatherData.field_id == field.id,

                WeatherData.recorded_date >= today

            ).first()





            if existing_weather:


                print(
                    f"Weather already exists today for field {field.id}"
                )


                continue





            weather = get_weather(
                field.location
            )





            new_weather = WeatherData(


                field_id = field.id,


                temperature = weather["temperature"],


                humidity = weather["humidity"],


                rainfall = weather["rainfall"],


                wind_speed = weather["wind_speed"],


                weather_condition = weather["weather_condition"]

            )




            db.add(
                new_weather
            )






        db.commit()



        print(
            "Weather data updated successfully"
        )



    except Exception as e:


        db.rollback()


        print(
            "Weather update failed:",
            e
        )



    finally:


        db.close()







def start_scheduler():



    # Run once when server starts

    fetch_all_weather()





    # Daily update at 6 AM

    scheduler.add_job(

        fetch_all_weather,

        "cron",

        hour=6,

        minute=0,

        id="daily_weather_update",

        replace_existing=True

    )



    scheduler.start()



    print(
        "Weather scheduler started"
    )