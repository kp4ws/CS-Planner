from fastapi import Depends
import uuid
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from api.users.models import User
from api.core.database import get_db
from api.core.config import settings
from api.core.exceptions import raise_401

# OAuth2PasswordBearer extracts the JWT token from the Authorization header
# tokenUrl tells FastAPI's /docs UI where the login endpoint is
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    #TODO function documentation needs updating
    """
    Dependency function that verifies the JWT token and returns the current user.
    
    Use this as a dependency on any route that requires authentication:
        current_user: User = Depends(get_current_user)
    
    Flow:
        1. OAuth2PasswordBearer extracts the token from the Authorization header
        2. Token is decoded and verified against the secret key
        3. User ID is extracted from the token payload (stored under "sub")
        4. User is looked up in the database by ID and active status is verified
        5. Returns the User object if valid, raises 401 if anything fails
    
    Raises:
        HTTPException 401: If token is invalid, expired, or user not found
    """
    try:
        # Decode and verify the JWT token using our secret key and algorithm
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        
        # Extract user ID from the "sub" claim in the token payload
        user_id_str: str = decoded_payload.get("sub")

        if user_id_str is None:
            raise_401()
            
    except JWTError:
        raise_401()
    
    try:
        user_id = uuid.UUID(user_id_str)
    except ValueError:
        raise_401()

    # Look up the user in the database
    query = select(User).where(User.id == user_id)
    user = db.execute(query).scalar_one_or_none()
    
    if user is None or not user.is_active:
        raise_401()
  
    return user