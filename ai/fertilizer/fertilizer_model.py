import joblib


model = joblib.load(

"ai/fertilizer/fertilizer_model.pkl"

)



def predict_fertilizer(data):


    result = model.predict(
        [
            data
        ]
    )


    probability = model.predict_proba(
        [
            data
        ]
    )


    confidence = max(probability[0])*100


    return {

        "fertilizer":result[0],

        "confidence":round(confidence,2)

    }
