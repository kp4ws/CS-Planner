from typing import Annotated

from clerk_backend_api import Clerk, AuthenticateRequestOptions
from clerk_backend_api.security.types import RequestState
from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from api.core.config import Settings, get_settings
from api.core.exceptions import raise_401
from api.core.database import get_db
from api.users.models import User

http_bearer = HTTPBearer(auto_error=False)

@lru_cache
def get_clerk_client() -> Clerk:
    return Clerk(bearer_auth=get_settings().CLERK_SECRET_KEY)

async def get_current_user(
        request: Request,
        settings: Annotated[Settings, Depends(get_settings)],
        db: Annotated[Session, Depends(get_db)],
        _creds: Annotated[HTTPAuthorizationCredentials | None, Depends(http_bearer)] = None,
) -> User:
    clerk_client: Clerk = get_clerk_client()

    request_state: RequestState = await clerk_client.authenticate_request_async(
        request,
        AuthenticateRequestOptions(
            authorized_parties=settings.CLERK_AUTHORIZED_PARTIES,
            accepts_token=["session_token"],
        ),
    )

    if not request_state.is_signed_in:
        raise_401(request_state.reason or "Could not validate credentials")
    
    clerk_id: str = request_state.payload.get("sub")
    
    if not clerk_id:
        raise_401("Invalid token payload")

    user = db.execute(
        select(User).where(
            User.clerk_id == clerk_id
        )
    ).scalar_one_or_none()

    #For first time users login (user is registered in Clerk but not yet in db)
    if not user:
        try:
            user = User(clerk_id = clerk_id)
            db.add(user)
            db.commit()
            db.refresh(user)
        except IntegrityError:
            db.rollback()
            user = db.execute(
                select(User).where(User.clerk_id == clerk_id)
            ).scalar_one_or_none()

    if not user or not user.is_active:
        raise_401("User not found or inactive")
    
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]
DBSession = Annotated[Session, Depends(get_db)]