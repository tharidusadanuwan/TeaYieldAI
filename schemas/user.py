from pydantic import BaseModel, EmailStr



class UserCreate(

    BaseModel

):


    username:str


    email:str


    mobile:str


    password:str




class UserLogin(

    BaseModel

):


    email:str


    password:str




class UserResponse(

    BaseModel

):


    id:int


    username:str


    email:str


    mobile:str


    class Config:


        from_attributes=True




class ForgotPasswordRequest(

    BaseModel

):


    email:EmailStr




class ResetPasswordRequest(

    BaseModel

):


    token:str


    new_password:str