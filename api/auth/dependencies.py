from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
import os
from dotenv import load_dotenv, find_dotenv
from jose import jwt
from users.models import User

load_dotenv(find_dotenv())

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = None
    try:
        decoded_payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
        username = decoded_payload.get("sub")
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")        
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return user