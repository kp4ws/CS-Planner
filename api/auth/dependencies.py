from fastapi import Depends, Request
from clerk_backend_api import Clerk
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.users.models import User
from api.core.database import get_db
from api.core.config import settings
from api.core.exceptions import raise_401

clerk_client = Clerk(bearer_auth=settings.CLERK_SECRET_KEY)

async def get_current_user(
        request: Request,
        db: Session = Depends(get_db)
):
    '''
    Validates the Clerk JWT from the request and returns the local DB user.
    '''
    request_state = await clerk_client.authenticate_request(request)

    if not request_state.is_signed_in:
        raise_401()

    clerk_id: str = request_state.payload.get("sub")

    query = select(User).where(User.clerk_id == clerk_id)
    user = db.execute(query).scalar_one_or_none()

    if not user or not user.is_active:
        raise_401()
    
    return user