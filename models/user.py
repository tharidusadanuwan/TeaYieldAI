from sqlalchemy import Column, Integer, String, Text, TIMESTAMP

from database import Base

from datetime import datetime



class User(Base):


    __tablename__ = "user_tbl"



    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(
        String(100),
        nullable=False
    )


    email = Column(
        String(150),
        unique=True,
        nullable=False
    )


    mobile = Column(
        String(20)
    )


    password_hash = Column(
        Text,
        nullable=False
    )


    created_at = Column(
        TIMESTAMP,
        default=datetime.utcnow
    )