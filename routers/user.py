from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import get_db

from models.user import User

from schemas.user_schema import (
    UserUpdate,
    PasswordUpdate
)


router = APIRouter(

    prefix="/api/user",

    tags=["User"]

)



# GET PROFILE

@router.get("/{user_id}")
def get_user(

    user_id:int,

    db:Session=Depends(get_db)

):


    user=db.query(User).filter(

        User.id==user_id

    ).first()



    if not user:

        raise HTTPException(

            status_code=404,

            detail="User not found"

        )


    return {


        "id":user.id,

        "username":user.username,

        "email":user.email,

        "mobile":user.mobile


    }






# UPDATE PROFILE

@router.put("/{user_id}")
def update_user(

    user_id:int,

    data:UserUpdate,

    db:Session=Depends(get_db)

):


    user=db.query(User).filter(

        User.id==user_id

    ).first()



    if not user:

        raise HTTPException(

            404,

            "User not found"

        )



    user.username=data.username

    user.email=data.email

    user.mobile=data.mobile



    db.commit()

    db.refresh(user)



    return {

        "message":"Profile updated successfully"

    }







# DELETE / LOGOUT SUPPORT

@router.delete("/{user_id}")
def delete_user(

    user_id:int,

    db:Session=Depends(get_db)

):


    user=db.query(User).filter(

        User.id==user_id

    ).first()



    if not user:

        raise HTTPException(

            404,

            "User not found"

        )



    db.delete(user)

    db.commit()


    return {

        "message":"User deleted"

    }