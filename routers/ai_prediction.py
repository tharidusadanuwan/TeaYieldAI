from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from database import get_db


from models.ai_prediction import AIPrediction


from schemas.ai_prediction_schema import (
    AIPredictionCreate,
    AIPredictionResponse
)




router = APIRouter(

    prefix="/api/predictions",

    tags=["AI Predictions"]

)





# =====================================
# Generate AI Predictions
# =====================================


@router.post("/generate")
def generate_ai_predictions(

    db: Session = Depends(get_db)

):


    # Lazy import
    # AI service loads only when endpoint is called

    from services.prediction_service import generate_predictions



    generate_predictions(db)



    return {


        "message":

        "Prediction generated"


    }









# =====================================
# Get Predictions
# =====================================


@router.get(

    "/",

    response_model=list[AIPredictionResponse]

)

def get_predictions(

    db: Session = Depends(get_db)

):


    return db.query(

        AIPrediction

    ).all()









# =====================================
# Create Manual Prediction
# =====================================


@router.post(

    "/",

    response_model=AIPredictionResponse

)

def create_prediction(

    prediction:AIPredictionCreate,

    db:Session=Depends(get_db)

):


    new_prediction=AIPrediction(

        **prediction.dict()

    )



    db.add(

        new_prediction

    )



    db.commit()



    db.refresh(

        new_prediction

    )



    return new_prediction