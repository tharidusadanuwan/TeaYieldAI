import joblib
import pandas as pd
import os



# =========================================
# Model Path
# =========================================


BASE_DIR = os.path.dirname(__file__)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "fertilizer_model.pkl"
)





# =========================================
# Lazy Model Loading
# =========================================


model = None



def get_model():

    global model


    if model is None:


        print(
            "Loading Fertilizer AI Model..."
        )


        model = joblib.load(
            MODEL_PATH
        )


        print(
            "Fertilizer AI Model Loaded Successfully"
        )



    return model







# =========================================
# Calculate Fertilizer Amount
# =========================================


def calculate_fertilizer_amount(data):


    nitrogen = data["nitrogen"]

    phosphorus = data["phosphorus"]

    potassium = data["potassium"]

    moisture = data["moisture"]



    amount = 20





    # Low nitrogen requires more fertilizer

    if nitrogen < 40:

        amount += 10


    elif nitrogen > 80:

        amount -= 5





    # Low phosphorus

    if phosphorus < 30:

        amount += 5





    # Low potassium

    if potassium < 30:

        amount += 5





    # High moisture reduce fertilizer amount

    if moisture > 80:

        amount -= 5





    if amount < 10:

        amount = 10




    return amount







# =========================================
# Calculate Application Time
# =========================================


def calculate_application_time(data):


    rainfall = data["rainfall"]

    humidity = data["humidity"]





    if rainfall > 50:


        return (

            "After heavy rainfall "
            "(2-3 days later)"

        )





    elif rainfall > 20:


        return (

            "After rainfall "
            "(next day)"

        )





    elif humidity > 80:


        return (

            "Early morning application"

        )





    else:


        return (

            "During dry soil condition"

        )









# =========================================
# AI Fertilizer Prediction
# =========================================


def predict_fertilizer(data):


    # Load model only when required

    fertilizer_model = get_model()





    input_data = pd.DataFrame([

        {


            "ph_level":

            data["soil_ph"],



            "nitrogen":

            data["nitrogen"],



            "phosphorus":

            data["phosphorus"],



            "potassium":

            data["potassium"],



            "moisture":

            data["moisture"],



            "organic_matter":

            data.get(

                "organic_matter",

                0

            ),



            "temperature":

            data["temperature"],



            "humidity":

            data.get(

                "humidity",

                0

            ),



            "rainfall":

            data["rainfall"]


        }

    ])









    # ML Prediction


    prediction = fertilizer_model.predict(

        input_data

    )





    confidence = fertilizer_model.predict_proba(

        input_data

    )





    confidence_score = round(

        max(confidence[0]) * 100,

        2

    )









    # Dynamic calculation


    amount = calculate_fertilizer_amount(

        data

    )





    application_time = calculate_application_time(

        data

    )









    return {



        "fertilizer":

        prediction[0],





        "confidence":

        confidence_score,





        "amount":

        amount,





        "application_time":

        application_time,





        "reason":

        (

        "AI recommendation generated "

        "based on soil nutrients, "

        "weather conditions, and "

        "field environmental factors"

        )



    }