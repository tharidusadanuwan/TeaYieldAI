from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles


from database import Base, engine





# ==========================
# Routers
# ==========================


from routers import auth

from routers import tea_fields

from routers import weather_router

from routers import soil

from routers import fertilizer

from routers import disease

from routers import yield_records

from routers import ai_prediction

from routers import dashboard

from routers import user







# ==========================
# Create Database Tables
# ==========================


Base.metadata.create_all(

    bind=engine

)







app = FastAPI(

    title="TeaYield AI API"

)









# ==========================
# CORS
# ==========================


app.add_middleware(

    CORSMiddleware,


    allow_origins=[

        "http://localhost:5173",

        "http://127.0.0.1:5173"

    ],


    allow_credentials=True,


    allow_methods=["*"],


    allow_headers=["*"]

)











# ==========================
# Startup Events
# ==========================


@app.on_event("startup")

def startup_event():


    print(

        "TeaYield AI API Started Successfully"

    )


    print(

        "Background AI schedulers disabled for Render free tier"

    )












# ==========================
# Include Routers
# ==========================


app.include_router(

    auth.router

)



app.include_router(

    tea_fields.router

)



app.include_router(

    weather_router.router

)



app.include_router(

    soil.router

)



app.include_router(

    fertilizer.router

)



app.include_router(

    disease.router

)



app.include_router(

    yield_records.router

)



app.include_router(

    ai_prediction.router

)



app.include_router(

    dashboard.router

)



app.include_router(

    user.router

)









# ==========================
# Static Files
# ==========================


app.mount(

    "/uploads",


    StaticFiles(

        directory="uploads"

    ),


    name="uploads"

)











# ==========================
# Root API
# ==========================


@app.get("/")

def root():


    return {


        "message":

        "TeaYield AI Backend Running"


    }