from fastapi import HTTPException, status

def raise_404(detail="Not found"):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

def raise_401(detail="Could not validate credentials"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )

def raise_403(detail="Not authorized"):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

def raise_400(detail="Bad request"):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

def raise_409(detail="Resource already exists or is in use"):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)