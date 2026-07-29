from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from database import get_db

from models.fertilizer import FertilizerUsage

from schemas.fertilizer import (
    FertilizerCreate,
    FertilizerUpdate
)



router = APIRouter(

    prefix="/api/fertilizer",

    tags=["Fertilizer"]

)





# CREATE

@router.post("/")
def create_fertilizer(

    fertilizer:FertilizerCreate,

    db:Session=Depends(get_db)

):


    new_fertilizer = FertilizerUsage(

        **fertilizer.dict()

    )


    db.add(new_fertilizer)

    db.commit()

    db.refresh(new_fertilizer)


    return new_fertilizer






# GET ALL


@router.get("/")
def get_fertilizers(

    db:Session=Depends(get_db)

):


    return db.query(
        FertilizerUsage
    ).all()






# GET ONE


@router.get("/{fertilizer_id}")
def get_fertilizer(

    fertilizer_id:int,

    db:Session=Depends(get_db)

):


    fertilizer = db.query(
        FertilizerUsage
    ).filter(

        FertilizerUsage.fertilizer_id == fertilizer_id

    ).first()



    if not fertilizer:

        raise HTTPException(

            status_code=404,

            detail="Fertilizer not found"

        )


    return fertilizer







# UPDATE


@router.put("/{fertilizer_id}")
def update_fertilizer(

    fertilizer_id:int,

    data:FertilizerUpdate,

    db:Session=Depends(get_db)

):


    fertilizer = db.query(
        FertilizerUsage
    ).filter(

        FertilizerUsage.fertilizer_id == fertilizer_id

    ).first()



    if not fertilizer:

        raise HTTPException(

            status_code=404,

            detail="Fertilizer not found"

        )



    for key,value in data.dict().items():

        setattr(
            fertilizer,
            key,
            value
        )


    db.commit()

    db.refresh(fertilizer)



    return fertilizer







# DELETE


@router.delete("/{fertilizer_id}")
def delete_fertilizer(

    fertilizer_id:int,

    db:Session=Depends(get_db)

):


    fertilizer = db.query(
        FertilizerUsage
    ).filter(

        FertilizerUsage.fertilizer_id == fertilizer_id

    ).first()



    if not fertilizer:

        raise HTTPException(

            status_code=404,

            detail="Fertilizer not found"

        )



    db.delete(fertilizer)

    db.commit()



    return {

        "message":
        "Fertilizer deleted successfully"

    }