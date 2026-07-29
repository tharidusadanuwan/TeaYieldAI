import os
import joblib

import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error





BASE_DIR = os.path.dirname(__file__)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "risk_model.pkl"
)





# =====================================
# Create Risk Model
# =====================================


def create_risk_model():


    """
    Train AI Risk Prediction Model

    Features:

    nitrogen
    phosphorus
    potassium
    moisture
    ph_level
    temperature
    humidity
    rainfall
    disease_score
    fertilizer_days


    Output:

    risk_score

    """



    dataset_path = os.path.join(

        BASE_DIR,

        "risk_dataset.csv"

    )





    if not os.path.exists(dataset_path):

        raise FileNotFoundError(

            "risk_dataset.csv not found"

        )






    data = pd.read_csv(

        dataset_path

    )






    X = data.drop(

        "risk_score",

        axis=1

    )



    y = data["risk_score"]







    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42

    )








    model = RandomForestRegressor(

        n_estimators=100,

        random_state=42

    )








    model.fit(

        X_train,

        y_train

    )









    prediction = model.predict(

        X_test

    )







    error = mean_absolute_error(

        y_test,

        prediction

    )




    print(

        "Risk Model MAE:",

        error

    )









    joblib.dump(

        model,

        MODEL_PATH

    )





    print(

        "Risk model saved successfully"

    )








if __name__ == "__main__":


    create_risk_model()
