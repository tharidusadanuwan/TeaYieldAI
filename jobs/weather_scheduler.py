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

        print(
            f"Starting weather update for {today}"
        )

        fields = db.query(
            TeaField
        ).all()

        print(
            f"Found {len(fields)} tea fields"
        )

        for field in fields:

            if not field.location:

                print(
                    f"Skipping field {field.id}: no location"
                )

                continue

            existing_weather = (
                db.query(
                    WeatherData
                )
                .filter(
                    WeatherData.field_id == field.id,
                    WeatherData.recorded_date >= today
                )
                .first()
            )

            if existing_weather:

                print(
                    f"Weather already exists today for field {field.id}"
                )

                continue

            try:

                weather = get_weather(
                    field.location
                )

                new_weather = WeatherData(

                    field_id=field.id,

                    temperature=weather["temperature"],

                    humidity=weather["humidity"],

                    rainfall=weather["rainfall"],

                    wind_speed=weather["wind_speed"],

                    weather_condition=weather["weather_condition"]

                )

                db.add(
                    new_weather
                )

                print(
                    f"Weather saved for field {field.id}"
                )

            except Exception as field_error:

                print(
                    f"Weather update failed for field {field.id}: {field_error}"
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

        raise

    finally:

        db.close()


def start_scheduler():

    print(
        "Starting local weather scheduler..."
    )

    # Run immediately when application starts

    fetch_all_weather()

    # Run every day at 6:00 AM

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
        "Weather scheduler started successfully"
    )
