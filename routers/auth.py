from fastapi import (

    APIRouter,

    Depends,

    HTTPException

)


from sqlalchemy.orm import Session


from database import get_db


from models.user import User


from schemas.user import (

    UserCreate,

    UserLogin,

    ForgotPasswordRequest,

    ResetPasswordRequest

)


from utils.security import (

    hash_password,

    verify_password,

    create_token,

    create_reset_token,

    verify_reset_token

)


from utils.email_service import (

    send_reset_email

)



router = APIRouter(

    prefix="/api/auth",

    tags=["Authentication"]

)





# REGISTER


@router.post(

    "/register"

)

def register(

    user:UserCreate,

    db:Session=Depends(

        get_db

    )

):


    existing_user = (

        db.query(User)

        .filter(

            User.email == user.email

        )

        .first()

    )



    if existing_user:


        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )



    new_user = User(


        username=user.username,


        email=user.email,


        mobile=user.mobile,


        password_hash=

        hash_password(

            user.password

        )

    )



    db.add(

        new_user

    )


    db.commit()


    db.refresh(

        new_user

    )



    return {


        "message":

        "User created successfully"

    }







# LOGIN


@router.post(

    "/login"

)

def login(

    user:UserLogin,

    db:Session=Depends(

        get_db

    )

):


    db_user = (

        db.query(User)

        .filter(

            User.email == user.email

        )

        .first()

    )



    if not db_user:


        raise HTTPException(

            status_code=401,

            detail="Invalid email or password"

        )



    password_correct = (

        verify_password(

            user.password,

            db_user.password_hash

        )

    )



    if not password_correct:


        raise HTTPException(

            status_code=401,

            detail="Invalid email or password"

        )



    token = create_token({

        "user_id":db_user.id

    })



    return {


        "access_token":token,


        "user_id":db_user.id,


        "username":db_user.username,


        "email":db_user.email

    }








# FORGOT PASSWORD


@router.post(

    "/forgot-password"

)

def forgot_password(

    data:ForgotPasswordRequest,

    db:Session=Depends(

        get_db

    )

):


    user = (

        db.query(User)

        .filter(

            User.email == data.email

        )

        .first()

    )



    message = (

        "If this email exists, "

        "a password reset link has been sent."

    )



    if not user:


        return {

            "message":message

        }



    reset_token = (

        create_reset_token(

            user.email

        )

    )



    reset_link = (

        "http://localhost:5173"

        "/reset-password"

        f"?token={reset_token}"

    )



    try:


        send_reset_email(

            receiver_email=user.email,

            reset_link=reset_link

        )


    except Exception as error:


        print(

            "EMAIL ERROR:",

            error

        )


        raise HTTPException(

            status_code=500,

            detail=(

                "Unable to send reset email. "

                "Check your email configuration."

            )

        )



    return {

        "message":message

    }








# RESET PASSWORD


@router.post(

    "/reset-password"

)

def reset_password(

    data:ResetPasswordRequest,

    db:Session=Depends(

        get_db

    )

):


    email = (

        verify_reset_token(

            data.token

        )

    )



    if not email:


        raise HTTPException(

            status_code=400,

            detail=(

                "This password reset link "

                "is invalid or has expired."

            )

        )



    user = (

        db.query(User)

        .filter(

            User.email == email

        )

        .first()

    )



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )



    if len(

        data.new_password

    ) < 6:


        raise HTTPException(

            status_code=400,

            detail=(

                "Password must contain "

                "at least 6 characters."

            )

        )



    user.password_hash = (

        hash_password(

            data.new_password

        )

    )



    db.commit()



    return {


        "message":

        "Password reset successfully. "

        "You can now log in."

    }