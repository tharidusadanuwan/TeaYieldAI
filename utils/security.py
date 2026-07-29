from passlib.context import CryptContext

from jose import jwt

from datetime import datetime, timedelta


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)


SECRET_KEY = "teayield-secret-key"

ALGORITHM = "HS256"


def hash_password(

    password:str

):

    return pwd_context.hash(

        password

    )



def verify_password(

    plain_password:str,

    hashed_password:str

):

    return pwd_context.verify(

        plain_password,

        hashed_password

    )



def create_token(

    data:dict

):

    return jwt.encode(

        data,

        SECRET_KEY,

        algorithm=ALGORITHM

    )



def create_reset_token(

    email:str

):

    expire = datetime.utcnow() + timedelta(

        minutes=30

    )


    payload = {

        "sub":email,

        "purpose":"password_reset",

        "exp":expire

    }


    return jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM

    )



def verify_reset_token(

    token:str

):

    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )


        if (

            payload.get("purpose")

            !=

            "password_reset"

        ):


            return None


        return payload.get("sub")


    except Exception:


        return None