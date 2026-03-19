from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    payload = data.copy()
    expires = datetime.now() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    payload.update({"exp": expires})
    encoded_jwt = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"))

    return encoded_jwt