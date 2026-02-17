from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
import os

app = FastAPI()

api_key_header = APIKeyHeader(name="Authorization", auto_error=True)


def verify_token(auth_header: str = Depends(api_key_header)):
    API_TOKEN = os.getenv("TOKEN")
    if auth_header != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication token",
        )
