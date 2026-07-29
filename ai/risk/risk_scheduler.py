from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime, timedelta

from database import SessionLocal

from services.risk_analysis_service import analyze_field_risk

from models.tea_field import TeaField

from models.risk_analysis import RiskAnalysis



scheduler = BackgroundScheduler()





def generate_risk_analysis():


    print(
        "Starting AI Risk Analysis generation..."
    )


    db = SessionLocal()


    try:


        fields = db.query(
            TeaField
        ).all()



        for field in fields:


            try:


                # Check latest risk analysis

                latest = (
                    db.query(RiskAnalysis)
                    .filter(
                        RiskAnalysis.field_id == field.id
                    )
                    .order_by(
                        RiskAnalysis.created_at.desc()
                    )
                    .first()
                )



                if latest:


                    days_difference = (
                        datetime.now()
                        -
                        latest.created_at
                    ).days



                    if days_difference < 7:


                        print(
                            f"Skipping Field {field.id} - Risk already generated {days_difference} days ago"
                        )

                        continue





                # Generate new risk

                analyze_field_risk(

                    db,

                    field.id

                )



                print(
                    f"Risk generated for Field {field.id}"
                )



            except Exception as e:


                print(
                    f"Risk failed for Field {field.id}:",
                    e
                )




    finally:


        db.close()








def start_risk_scheduler():



    # Run immediately when backend starts

    generate_risk_analysis()




    # Then check every day

    scheduler.add_job(

        generate_risk_analysis,

        trigger="interval",

        days=1,

        id="weekly_risk_analysis",

        replace_existing=True

    )



    scheduler.start()



    print(
        "Weekly AI Risk Scheduler Started"
    )