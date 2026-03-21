from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
import os
from dotenv import load_dotenv, find_dotenv
from jose import jwt
from users.models import User

load_dotenv(find_dotenv())

# OAuth2PasswordBearer extracts the JWT token from the Authorization header
# tokenUrl tells FastAPI's /docs UI where the login endpoint is
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Dependency function that verifies the JWT token and returns the current user.
    
    Use this as a dependency on any route that requires authentication:
        current_user: User = Depends(get_current_user)
    
    Flow:
        1. OAuth2PasswordBearer extracts the token from the Authorization header
        2. Token is decoded and verified against the secret key
        3. Username is extracted from the token payload (stored under "sub")
        4. User is looked up in the database by username
        5. Returns the User object if valid, raises 401 if anything fails
    
    Raises:
        HTTPException 401: If token is invalid, expired, or user not found
    """
    user = None
    try:
        # Decode and verify the JWT token using our secret key and algorithm
        decoded_payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
        
        # Extract username from the "sub" claim in the token payload
        username = decoded_payload.get("sub")

        # Look up the user in the database
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")     
           
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return user