from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.tea_field import TeaField
from schemas.tea_field import TeaFieldCreate, TeaFieldUpdate


router = APIRouter(
    prefix="/api/fields",
    tags=["Tea Fields"]
)


@router.post("/")
def create_field(
    field: TeaFieldCreate,
    db: Session = Depends(get_db)
):

    new_field = TeaField(
        **field.dict()
    )

    db.add(new_field)
    db.commit()
    db.refresh(new_field)

    return new_field



@router.get("/")
def get_fields(
    db: Session = Depends(get_db)
):

    return db.query(TeaField).all()



@router.put("/{field_id}")
def update_field(
    field_id: int,
    field: TeaFieldUpdate,
    db: Session = Depends(get_db)
):

    existing_field = db.query(TeaField).filter(
    TeaField.id == field_id
).first()


    if not existing_field:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )


    for key, value in field.dict().items():

        setattr(
            existing_field,
            key,
            value
        )


    db.commit()
    db.refresh(existing_field)


    return existing_field


@router.delete("/{field_id}")
def delete_field(
    field_id:int,
    db:Session=Depends(get_db)
):

    field = db.query(TeaField).filter(
        TeaField.id == field_id
    ).first()


    if not field:

        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )


    db.delete(field)

    db.commit()


    return {
        "message":"Field deleted successfully"
    }