from apscheduler.schedulers.background import BackgroundScheduler

from database import SessionLocal

from services.prediction_service import generate_predictions


scheduler = BackgroundScheduler()



def run_prediction_job():

    db = SessionLocal()

    try:

        generate_predictions(db)

    finally:

        db.close()





def start_prediction_scheduler():


    # Run immediately when backend starts

    run_prediction_job()



    # Run every day at 6 AM

    scheduler.add_job(

        run_prediction_job,

        "cron",

        hour=6,

        minute=0

    )


    scheduler.start()


    print(
        "AI Prediction Scheduler Started"
    )