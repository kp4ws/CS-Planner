from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.v1.endpoints import v1_router
from api.core.config import settings

# Manages app startup and shutdown lifecycle
# Code before yield runs on startup, after yield runs on shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    Ensures all models are "seen" by the Base on startup.
    Triggers api/models/__init__.py for importing all models defined in that file.
    '''
    import models
    yield

app = FastAPI(title="TODO: Name", lifespan=lifespan)

allowed_origins = settings.ALLOWED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

#TODO Add exception handling

#Register v1 router
app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "API is running"}