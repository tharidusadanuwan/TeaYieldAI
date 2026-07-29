from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import get_db

from models.soil import SoilData

from schemas.soil import SoilCreate



router = APIRouter(

    prefix="/api/soil",

    tags=["Soil Data"]

)



# CREATE


@router.post("/")
def create_soil(

    soil:SoilCreate,

    db:Session=Depends(get_db)

):


    new_soil = SoilData(

        **soil.dict()

    )


    db.add(new_soil)

    db.commit()

    db.refresh(new_soil)


    return new_soil





# READ ALL


@router.get("/")
def get_soil(

    db:Session=Depends(get_db)

):

    return db.query(SoilData).all()



@router.delete("/{soil_id}")
def delete_soil(
    soil_id:int,
    db:Session=Depends(get_db)
):

    soil = db.query(SoilData).filter(
        SoilData.soil_id == soil_id
    ).first()


    if not soil:

        raise HTTPException(
            status_code=404,
            detail="Soil data not found"
        )


    db.delete(soil)

    db.commit()


    return {
        "message":"Soil data deleted successfully"
    }


# UPDATE

@router.put("/{soil_id}")
def update_soil(
    soil_id:int,
    soil:SoilCreate,
    db:Session=Depends(get_db)
):

    db_soil = db.query(SoilData).filter(
        SoilData.soil_id == soil_id
    ).first()


    if not db_soil:

        raise HTTPException(
            status_code=404,
            detail="Soil data not found"
        )


    db_soil.field_id = soil.field_id
    db_soil.soil_type = soil.soil_type
    db_soil.ph_level = soil.ph_level
    db_soil.nitrogen = soil.nitrogen
    db_soil.phosphorus = soil.phosphorus
    db_soil.potassium = soil.potassium
    db_soil.moisture = soil.moisture
    db_soil.organic_matter = soil.organic_matter


    db.commit()

    db.refresh(db_soil)


    return db_soil


@router.delete("/{soil_id}")
def delete_soil(
    soil_id:int,
    db:Session=Depends(get_db)
):

    soil = db.query(SoilData).filter(
        SoilData.soil_id == soil_id
    ).first()


    if not soil:
        raise HTTPException(
            status_code=404,
            detail="Soil data not found"
        )


    db.delete(soil)

    db.commit()


    return {
        "message":"Soil data deleted successfully"
    }