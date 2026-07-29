from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.fertilizer_recommendation import FertilizerRecommendation

from schemas.ai_fertilizer import FertilizerRecommendationRequest

from services.fertilizer_ai_service import (
    generate_fertilizer_recommendation
)



router = APIRouter(

    prefix="/api/ai/fertilizer",

    tags=["AI Fertilizer Recommendation"]

)





# =====================================================
# Generate AI Fertilizer Recommendation
# =====================================================


@router.post("/recommendation")
def fertilizer_recommendation(

    data: FertilizerRecommendationRequest,

    db: Session = Depends(get_db)

):


    result = generate_fertilizer_recommendation(

        data.field_id,

        db

    )





    if not result:


        raise HTTPException(

            status_code=404,

            detail="Unable to generate fertilizer recommendation. Missing field data."

        )








    recommendation = FertilizerRecommendation(


        field_id=data.field_id,


        recommended_fertilizer=result["fertilizer"],


        recommended_amount=result["amount"],


        application_time=result["application_time"],


        reason=result["reason"],


        confidence_score=float(result["confidence"])

    )





    db.add(recommendation)


    db.commit()


    db.refresh(recommendation)








    return {


        "message":
        "AI Fertilizer recommendation generated successfully",


        "recommendation_id":
        recommendation.recommendation_id,


        "fertilizer":
        recommendation.recommended_fertilizer,


        "amount":
        recommendation.recommended_amount,


        "application_time":
        recommendation.application_time,


        "confidence":
        recommendation.confidence_score,


        "reason":
        recommendation.reason


    }









# =====================================================
# Get Fertilizer Recommendation History
# =====================================================


@router.get("/recommendations")
def get_fertilizer_recommendations(

    db: Session = Depends(get_db)

):


    recommendations = (

        db.query(
            FertilizerRecommendation
        )

        .order_by(

            FertilizerRecommendation.created_at.desc()

        )

        .all()

    )


    return recommendations










# =====================================================
# Get Single Recommendation
# =====================================================


@router.get("/recommendations/{recommendation_id}")
def get_single_recommendation(

    recommendation_id:int,

    db:Session = Depends(get_db)

):


    recommendation = (

        db.query(

            FertilizerRecommendation

        )

        .filter(

            FertilizerRecommendation.recommendation_id

            ==

            recommendation_id

        )

        .first()

    )




    if not recommendation:


        raise HTTPException(

            status_code=404,

            detail="Recommendation not found"

        )




    return recommendation











# =====================================================
# Delete Recommendation
# =====================================================


@router.delete("/recommendation/{recommendation_id}")
def delete_fertilizer_recommendation(

    recommendation_id:int,

    db:Session = Depends(get_db)

):


    recommendation = (

        db.query(

            FertilizerRecommendation

        )

        .filter(

            FertilizerRecommendation.recommendation_id

            ==

            recommendation_id

        )

        .first()

    )





    if not recommendation:


        raise HTTPException(

            status_code=404,

            detail="Fertilizer recommendation not found"

        )





    db.delete(recommendation)


    db.commit()





    return {


        "message":

        "Fertilizer recommendation deleted successfully"


    }