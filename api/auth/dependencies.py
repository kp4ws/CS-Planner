from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from api.users.models import User
from api.core.database import get_db
from api.core.config import settings

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
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode and verify the JWT token using our secret key and algorithm
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        
        # Extract username from the "sub" claim in the token payload
        username: str = decoded_payload.get("sub")

        if username is None:
            raise credentials_exception
           
    except JWTError:
        raise credentials_exception
    
    # Look up the user in the database
    query = select(User).where(User.username == username)
    user = db.execute(query).scalar_one_or_none()
    
    if user is None:
        raise credentials_exception
  
    return user