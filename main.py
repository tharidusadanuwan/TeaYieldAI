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
from routers import disease_ai
from routers import risk_analysis
from routers import dashboard
from routers import user

# ==========================

# Create Database Tables

# ==========================

Base.metadata.create_all(
bind=engine
)

# ==========================

# Create FastAPI Application

# ==========================

app = FastAPI(
title="TeaYield AI API"
)

# ==========================

# CORS

# ==========================

ALLOWED_ORIGINS = [
"http://localhost:5173",
"http://127.0.0.1:5173",
"https://tea-yield-ai-frontend.vercel.app"
]

app.add_middleware(
CORSMiddleware,
allow_origins=ALLOWED_ORIGINS,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]
)

# ==========================

# CORS Test

# ==========================

@app.get("/cors-test")
def cors_test():
return {
"message": "CORS test successful"
}

# ==========================

# Startup

# ==========================

@app.on_event("startup")
def startup_event():


print(
    "TeaYield AI API started successfully"
)

print(
    "CORS allowed origins:",
    ALLOWED_ORIGINS
)

# IMPORTANT:
# Do NOT start background schedulers here
# on the Render web service.
#
# Weather scheduler:
# start_scheduler()
#
# AI prediction scheduler:
# start_prediction_scheduler()
#
# Risk scheduler:
# start_risk_scheduler()


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
disease_ai.router
)

app.include_router(
risk_analysis.router
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

```
return {
    "message": "TeaYield AI Backend Running"
}

