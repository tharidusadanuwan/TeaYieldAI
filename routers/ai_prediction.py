from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from database import get_db

from models.ai_prediction import AIPrediction

from schemas.ai_prediction_schema import (
    AIPredictionCreate,
    AIPredictionResponse
)

from services.prediction_service import generate_predictions



router = APIRouter(

    prefix="/api/predictions",

    tags=["AI Predictions"]

)



@router.post("/generate")
def generate_ai_predictions(

    db:Session = Depends(get_db)

):


    generate_predictions(db)


    return {

        "message":
        "Prediction generated"

    }




@router.get(
"/",
response_model=list[AIPredictionResponse]
)
def get_predictions(

db:Session=Depends(get_db)

):


    return db.query(
        AIPrediction
    ).all()




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