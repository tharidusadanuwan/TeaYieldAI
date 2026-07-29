from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric,
    String,
    DateTime
)

from sqlalchemy.sql import func


from database import Base




class WeatherData(Base):

    __tablename__ = "weather_data"



    weather_id = Column(

        Integer,

        primary_key=True,

        index=True

    )



    field_id = Column(

        Integer,

        ForeignKey(
            "tea_fields.id",
            ondelete="CASCADE"
        ),

        nullable=False

    )



    temperature = Column(

        Numeric(
            5,
            2
        ),

        nullable=True

    )



    humidity = Column(

        Numeric(
            5,
            2
        ),

        nullable=True

    )



    rainfall = Column(

        Numeric(
            6,
            2
        ),

        nullable=True

    )



    wind_speed = Column(

        Numeric(
            5,
            2
        ),

        nullable=True

    )



    weather_condition = Column(

        String(
            100
        ),

        nullable=True

    )



    recorded_date = Column(

        DateTime,

        server_default=func.now()

    )