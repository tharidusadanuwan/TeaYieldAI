from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import get_db

from models.yield_record import YieldRecord

from schemas.yield_record import (
    YieldRecordCreate,
    YieldRecordUpdate
)



router = APIRouter(

    prefix="/api/yields",

    tags=["Yield Records"]

)





@router.post("/")
def create_yield(

    yield_data:YieldRecordCreate,

    db:Session=Depends(get_db)

):


    new_yield = YieldRecord(

        **yield_data.dict()

    )


    db.add(new_yield)

    db.commit()

    db.refresh(new_yield)


    return new_yield








@router.get("/")
def get_yields(

    db:Session=Depends(get_db)

):


    return db.query(
        YieldRecord
    ).all()









@router.get("/{yield_id}")
def get_yield(

    yield_id:int,

    db:Session=Depends(get_db)

):


    record = db.query(
        YieldRecord
    ).filter(

        YieldRecord.yield_id == yield_id

    ).first()



    if not record:

        raise HTTPException(

            status_code=404,

            detail="Yield record not found"

        )


    return record










@router.put("/{yield_id}")
def update_yield(

    yield_id:int,

    yield_data:YieldRecordUpdate,

    db:Session=Depends(get_db)

):


    record = db.query(
        YieldRecord
    ).filter(

        YieldRecord.yield_id == yield_id

    ).first()



    if not record:

        raise HTTPException(

            status_code=404,

            detail="Yield record not found"

        )



    for key,value in yield_data.dict().items():

        setattr(
            record,
            key,
            value
        )


    db.commit()

    db.refresh(record)


    return record











@router.delete("/{yield_id}")
def delete_yield(

    yield_id:int,

    db:Session=Depends(get_db)

):


    record = db.query(
        YieldRecord
    ).filter(

        YieldRecord.yield_id == yield_id

    ).first()



    if not record:

        raise HTTPException(

            status_code=404,

            detail="Yield record not found"

        )



    db.delete(record)

    db.commit()



    return {

        "message":
        "Yield record deleted successfully"

    }