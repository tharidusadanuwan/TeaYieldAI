import os

import joblib

import numpy as np





BASE_DIR = os.path.dirname(__file__)


MODEL_PATH = os.path.join(

    BASE_DIR,

    "risk_model.pkl"

)







# =====================================
# Load Model
# =====================================


if os.path.exists(MODEL_PATH):


    model = joblib.load(

        MODEL_PATH

    )


else:

    model = None











# =====================================
# Risk Prediction
# =====================================


def predict_risk(data:dict):


    """
    Input:

    {
        nitrogen:40,
        phosphorus:30,
        potassium:25,
        moisture:50,
        ph_level:6,
        temperature:28,
        humidity:70,
        rainfall:120,
        disease_score:20,
        fertilizer_days:30
    }


    Return:

    {
        risk_score:45,
        risk_level:"Medium"
    }

    """




    if model is None:


        return {

            "risk_score":50,

            "risk_level":"Medium"

        }





    features=[


        data["nitrogen"],


        data["phosphorus"],


        data["potassium"],


        data["moisture"],


        data["ph_level"],


        data["temperature"],


        data["humidity"],


        data["rainfall"],


        data["disease_score"],


        data["fertilizer_days"]


    ]







    input_data=np.array(

        features

    ).reshape(

        1,-1

    )







    score=model.predict(

        input_data

    )[0]







    score=round(

        float(score),

        2

    )







    return {


        "risk_score":

        score,


        "risk_level":

        get_risk_level(

            score

        )


    }












# =====================================
# Risk Category
# =====================================


def get_risk_level(score):


    if score >=75:

        return "High"



    elif score >=45:

        return "Medium"



    else:

        return "Low"