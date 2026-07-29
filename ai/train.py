import os

import joblib


from sklearn.model_selection import train_test_split


from sklearn.metrics import (

    mean_absolute_error,

    mean_squared_error,

    r2_score

)



from ai.dataset import load_dataset


from ai.model import (

    create_random_forest,

    create_xgboost

)





MODEL_PATH = "ai/saved_model.pkl"







def evaluate_model(

    name,

    model,

    X_test,

    y_test

):


    predictions = model.predict(

        X_test

    )



    mae = mean_absolute_error(

        y_test,

        predictions

    )



    rmse = mean_squared_error(

        y_test,

        predictions,

        squared=False

    )



    r2 = r2_score(

        y_test,

        predictions

    )




    print("\n====================")

    print(
        name
    )

    print("====================")



    print(

        "MAE:",

        mae

    )


    print(

        "RMSE:",

        rmse

    )


    print(

        "R² Score:",

        r2

    )



    return r2










def train_model():



    print(
        "Loading dataset..."
    )



    dataset = load_dataset()



    if dataset.empty:


        raise Exception(

            "Dataset empty"

        )







    X = dataset.drop(

        [

            "tea_yield",

            "field_id",

            "harvest_date",

            "weather_condition"

        ],

        axis=1

    )




    y = dataset["tea_yield"]







    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42

    )







    # =========================
    # RANDOM FOREST
    # =========================


    rf_model = create_random_forest()



    rf_model.fit(

        X_train,

        y_train

    )





    rf_score = evaluate_model(

        "Random Forest",

        rf_model,

        X_test,

        y_test

    )









    # =========================
    # XGBOOST
    # =========================


    xgb_model = create_xgboost()



    xgb_model.fit(

        X_train,

        y_train

    )





    xgb_score = evaluate_model(

        "XGBoost",

        xgb_model,

        X_test,

        y_test

    )








    # =========================
    # SELECT BEST MODEL
    # =========================


    if xgb_score > rf_score:


        best_model = xgb_model


        print(

            "Best Model: XGBoost"

        )


    else:


        best_model = rf_model


        print(

            "Best Model: Random Forest"

        )









    os.makedirs(

        "ai",

        exist_ok=True

    )





    joblib.dump(

        best_model,

        MODEL_PATH

    )





    print(

        "Model saved successfully"

    )










if __name__ == "__main__":


    train_model()