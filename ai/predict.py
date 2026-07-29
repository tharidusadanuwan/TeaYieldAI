import os
import joblib
import pandas as pd


MODEL_PATH = os.path.join(
    "ai",
    "saved_model.pkl"
)


model = joblib.load(
    MODEL_PATH
)



def predict_yield(data):


    # All available features from backend

    input_features = {

        "temperature":
        data["temperature"],


        "humidity":
        data["humidity"],


        "rainfall":
        data["rainfall"],


        "wind_speed":
        data["wind_speed"],


        # model expects soil_ph

        "soil_ph":
        data.get(
            "soil_ph",
            data.get("ph_level")
        ),


        "nitrogen":
        data["nitrogen"],


        "phosphorus":
        data.get(
            "phosphorus",
            0
        ),


        "potassium":
        data.get(
            "potassium",
            0
        ),


        "fertilizer_amount":
        data.get(
            "fertilizer_amount",
            0
        ),


        "month":
        data.get(
            "month",
            1
        ),


        "season":
        data.get(
            "season",
            1
        ),


        "soil_quality_score":
        data.get(
            "soil_quality_score",
            0
        ),


        "fertilizer_efficiency":
        data.get(
            "fertilizer_efficiency",
            1
        ),


        "previous_yield":
        data.get(
            "previous_yield",
            0
        )

    }



    # Convert to dataframe

    input_df = pd.DataFrame(
        [input_features]
    )



    # ===============================
    # IMPORTANT FIX
    # Match training features
    # ===============================

    if hasattr(model, "feature_names_in_"):


        trained_features = list(
            model.feature_names_in_
        )


        input_df = input_df[
            trained_features
        ]



    prediction = model.predict(
        input_df
    )



    return round(

        float(
            prediction[0]
        ),

        2

    )