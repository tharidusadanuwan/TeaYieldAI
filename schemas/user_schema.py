from pydantic import BaseModel


class UserUpdate(BaseModel):

    username:str

    email:str

    mobile:str



class PasswordUpdate(BaseModel):

    old_password:str

    new_password:str