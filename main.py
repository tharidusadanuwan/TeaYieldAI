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

#from routers import ai_prediction

#from routers import fertilizer_ai

#from routers import disease_ai

#from routers import risk_analysis

from routers import dashboard

from routers import user

# ==========================
# Schedulers
# ==========================


from jobs.weather_scheduler import start_scheduler

from ai.scheduler import start_prediction_scheduler

from ai.risk.risk_scheduler import start_risk_scheduler






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
        "Starting TeaYield AI Services..."
    )

    # Weather Scheduler
    #start_scheduler()

    # AI Yield Prediction Scheduler
    #start_prediction_scheduler()

    # AI Risk Analysis Scheduler
    #start_risk_scheduler()

    print(
        "All AI Services Started Successfully"
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



#app.include_router(

#    ai_prediction.router

#)



#app.include_router(

#    fertilizer_ai.router

#)



#app.include_router(

#    disease_ai.router

#)



#app.include_router(

#   risk_analysis.router

#)


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
