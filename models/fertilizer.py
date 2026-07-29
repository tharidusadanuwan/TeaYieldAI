from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey

from sqlalchemy.sql import func

from database import Base



class FertilizerUsage(Base):

    __tablename__ = "fertilizer_usage"



    fertilizer_id = Column(
        Integer,
        primary_key=True,
        index=True
    )



    field_id = Column(
        Integer,
        ForeignKey("tea_fields.id"),
        nullable=False
    )



    fertilizer_type = Column(
        String(100),
        nullable=False
    )



    application_method = Column(
        String(100)
    )



    quantity = Column(
        Float
    )



    unit = Column(
        String(20)
    )



    application_date = Column(
        DateTime,
        server_default=func.now()
    )



    nitrogen_content = Column(
        Float
    )



    phosphorus_content = Column(
        Float
    )



    potassium_content = Column(
        Float
    )



    notes = Column(
        Text
    )