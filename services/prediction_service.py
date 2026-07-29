from sqlalchemy.orm import Session


from models.tea_field import TeaField
from models.weather import WeatherData
from models.soil import SoilData
from models.fertilizer import FertilizerUsage
from models.yield_record import YieldRecord

from models.ai_prediction import AIPrediction


from ai.predict import predict_yield


from datetime import datetime, date





def generate_predictions(db: Session):


    print(
        "Starting AI prediction generation..."
    )



    fields = db.query(
        TeaField
    ).all()



    today = datetime.utcnow().date()





    for field in fields:


        try:


            # ==========================
            # WEATHER DATA
            # ==========================

            weather = db.query(
                WeatherData
            ).filter(

                WeatherData.field_id == field.id

            ).order_by(

                WeatherData.recorded_date.desc()

            ).first()





            # ==========================
            # SOIL DATA
            # ==========================

            soil = db.query(
                SoilData
            ).filter(

                SoilData.field_id == field.id

            ).first()





            # ==========================
            # FERTILIZER DATA
            # ==========================

            fertilizer = db.query(
                FertilizerUsage
            ).filter(

                FertilizerUsage.field_id == field.id

            ).order_by(

                FertilizerUsage.fertilizer_id.desc()

            ).first()





            # ==========================
            # PREVIOUS HARVEST
            # ==========================

            previous_yield = db.query(
                YieldRecord
            ).filter(

                YieldRecord.field_id == field.id

            ).order_by(

                YieldRecord.harvest_date.desc()

            ).first()






            if not weather or not soil:


                print(
                    f"Skipping Field {field.id} - Missing data"
                )

                continue





            # ==========================
            # DUPLICATE CHECK
            # ==========================

            existing = db.query(
                AIPrediction
            ).filter(

                AIPrediction.field_id == field.id,

                AIPrediction.prediction_date == today

            ).first()



            if existing:


                print(
                    f"Prediction already exists for Field {field.id}"
                )

                continue






            # ==========================
            # ML FEATURES
            # ==========================


            data = {


                "temperature":
                weather.temperature,


                "humidity":
                weather.humidity,


                "rainfall":
                weather.rainfall,


                "wind_speed":
                weather.wind_speed,



                "ph_level":
                soil.ph_level,


                "nitrogen":
                soil.nitrogen,


                "phosphorus":
                soil.phosphorus,


                "potassium":
                soil.potassium,



                "fertilizer_amount":

                fertilizer.quantity
                if fertilizer
                else 0,



                "month":
                today.month,



                "season":
                1,



                "soil_quality_score":

                (
                    soil.nitrogen
                    +
                    soil.phosphorus
                    +
                    soil.potassium
                )
                /
                3,



                "fertilizer_efficiency":
                1,



                "previous_yield":

                previous_yield.tea_weight

                if previous_yield

                else 0

            }







            # ==========================
            # MODEL PREDICTION
            # ==========================


            predicted = predict_yield(

                data

            )







            # ==========================
            # SAVE RESULT
            # ==========================


            prediction = AIPrediction(


                field_id=field.id,


                predicted_yield=predicted,


                confidence_score=90,


                risk_level="Low",


                recommendation=
                "Maintain current farming conditions",


                model_version=
                "XGBoost",


                prediction_date=today

            )



            db.add(
                prediction
            )



            print(

                f"Prediction created for Field {field.id}: {predicted} kg"

            )





        except Exception as e:


            db.rollback()


            print(

                "Prediction failed:",

                field.id,

                e

            )






    db.commit()



    print(

        "AI prediction generation completed"

    )