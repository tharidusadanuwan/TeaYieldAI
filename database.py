from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://neondb_owner:npg_Ac4yNFXa0VIP@ep-holy-term-auv5q11x-pooler.c-10.us-east-1.aws.neon.tech/TeaYieldAl?sslmode=require&channel_binding=require"


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()