from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import get_db

from models.disease import DiseaseDetection

from schemas.disease import (
    DiseaseCreate,
    DiseaseUpdate
)



router = APIRouter(

    prefix="/api/disease",

    tags=["Disease Detection"]

)





# CREATE

from fastapi import UploadFile, File, Form
import shutil
import os


@router.post("/")
def create_disease(

    field_id:int = Form(...),

    disease_name:str = Form(...),

    severity:str = Form(...),

    confidence_score:float = Form(...),

    affected_area:float = Form(...),

    treatment:str = Form(...),

    symptoms:str = Form(...),

    notes:str = Form(None),

    image:UploadFile = File(None),

    db:Session=Depends(get_db)

):


    image_path = None


    if image:

        os.makedirs(
            "uploads",
            exist_ok=True
        )


        image_path = f"uploads/{image.filename}"


        with open(
            image_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                image.file,
                buffer
            )



    new_disease = DiseaseDetection(

        field_id=field_id,

        disease_name=disease_name,

        severity=severity,

        confidence_score=confidence_score,

        affected_area=affected_area,

        treatment=treatment,

        symptoms=symptoms,

        image_url=image_path,

        notes=notes

    )


    db.add(new_disease)

    db.commit()

    db.refresh(new_disease)


    return new_disease






# GET ALL


@router.get("/")
def get_diseases(

    db:Session=Depends(get_db)

):


    return db.query(
        DiseaseDetection
    ).all()







# GET ONE


@router.get("/{disease_id}")
def get_disease(

    disease_id:int,

    db:Session=Depends(get_db)

):


    disease = db.query(
        DiseaseDetection
    ).filter(

        DiseaseDetection.disease_id == disease_id

    ).first()



    if not disease:

        raise HTTPException(

            status_code=404,

            detail="Disease record not found"

        )


    return disease







# UPDATE


@router.put("/{disease_id}")
def update_disease(

    disease_id:int,

    disease:DiseaseUpdate,

    db:Session=Depends(get_db)

):


    existing = db.query(
        DiseaseDetection
    ).filter(

        DiseaseDetection.disease_id == disease_id

    ).first()



    if not existing:

        raise HTTPException(

            status_code=404,

            detail="Disease record not found"

        )




    for key,value in disease.dict().items():

        setattr(
            existing,
            key,
            value
        )


    db.commit()

    db.refresh(existing)


    return existing







# DELETE


@router.delete("/{disease_id}")
def delete_disease(

    disease_id:int,

    db:Session=Depends(get_db)

):


    disease = db.query(
        DiseaseDetection
    ).filter(

        DiseaseDetection.disease_id == disease_id

    ).first()



    if not disease:

        raise HTTPException(

            status_code=404,

            detail="Disease record not found"

        )


    db.delete(disease)

    db.commit()



    return {

        "message":
        "Disease deleted successfully"

    }