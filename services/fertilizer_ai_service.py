from ai.fertilizer.predict_fertilizer import predict_fertilizer


from models.soil import SoilData

from models.weather import WeatherData

from models.fertilizer import FertilizerUsage





def generate_fertilizer_recommendation(

    field_id:int,

    db

):


    # ==============================
    # Get latest soil data
    # ==============================


    soil = db.query(

        SoilData

    ).filter(

        SoilData.field_id == field_id

    ).order_by(

        SoilData.recorded_date.desc()

    ).first()





    # ==============================
    # Get latest weather data
    # ==============================


    weather = db.query(

        WeatherData

    ).filter(

        WeatherData.field_id == field_id

    ).order_by(

        WeatherData.recorded_date.desc()

    ).first()





    # ==============================
    # Get fertilizer history
    # ==============================


    fertilizer_history = db.query(

        FertilizerUsage

    ).filter(

        FertilizerUsage.field_id == field_id

    ).all()






    if not soil:

        raise Exception(
            "Soil data not found for this field"
        )



    if not weather:

        raise Exception(
            "Weather data not found for this field"
        )






    # ==============================
    # Prepare ML Features
    # ==============================


    input_data = {


        "soil_ph":

        soil.ph_level or 0,



        "nitrogen":

        soil.nitrogen or 0,



        "phosphorus":

        soil.phosphorus or 0,



        "potassium":

        soil.potassium or 0,



        "moisture":

        soil.moisture or 0,



        "organic_matter":

        soil.organic_matter or 0,



        "temperature":

        float(weather.temperature or 0),



        "humidity":

        float(weather.humidity or 0),



        "rainfall":

        float(weather.rainfall or 0)

    }





    # ==============================
    # AI Prediction
    # ==============================


    prediction = predict_fertilizer(

        input_data

    )



    return prediction