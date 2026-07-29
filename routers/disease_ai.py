from fastapi import (

    APIRouter,

    Depends,

    UploadFile,

    File,

    Form

)


from sqlalchemy.orm import Session


from database import get_db


from services.disease_ai_service import (

    detect_disease

)





router = APIRouter(


    prefix="/api/ai/disease",


    tags=["AI Disease Detection"]


)









# =========================================
# Detect Disease
# =========================================


@router.post("/detect")

def disease_detection(


    field_id:int = Form(...),


    image:UploadFile = File(...),


    db:Session = Depends(get_db)

):



    result = detect_disease(


        field_id,


        image,


        db


    )



    return result










# =========================================
# Get Disease History
# =========================================


@router.get("/history")

def disease_history(


    db:Session = Depends(get_db)

):


    from models.disease_detection import DiseaseDetection



    data = db.query(

        DiseaseDetection

    ).order_by(

        DiseaseDetection.detected_at.desc()

    ).all()



    return data










# =========================================
# Delete Detection
# =========================================


@router.delete("/{detection_id}")

def delete_detection(


    detection_id:int,


    db:Session = Depends(get_db)

):


    from models.disease_detection import DiseaseDetection



    detection = db.query(

        DiseaseDetection

    ).filter(

        DiseaseDetection.detection_id == detection_id

    ).first()




    if not detection:


        return {


            "message":

            "Detection not found"

        }




    db.delete(detection)


    db.commit()



    return {


        "message":

        "Disease detection deleted successfully"

    }