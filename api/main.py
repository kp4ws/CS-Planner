from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router
from users.routes import router as user_router
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#TODO Seed mock data into database for development
def seed_data():
    pass

# Manages app startup and shutdown lifecycle
# Code before yield runs on startup, after yield runs on shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    import models
    seed_data()
    yield

app = FastAPI(lifespan=lifespan)

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

#TODO Add exception handling

#Register routers
app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "API is running"}