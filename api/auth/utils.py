import bcrypt
from jose import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def hash_password(password: str):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_access_token(data: dict):
    payload = data.copy()
    expires = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    payload.update({"exp": expires})
    encoded_jwt = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"))

    return encoded_jwt