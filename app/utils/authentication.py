from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def generate_jwt_token(data: dict) -> str:
    """Generate a JWT token with expiration."""
    to_encode = data.copy()
    expire_time = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire_time": expire_time.timestamp()})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_jwt_token(token: str) -> str | None:
    """Decode and validate a JWT token."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("expire_time") >= datetime.now().timestamp():
            return payload
    except JWTError:
        return None


def get_current_user(token: str = Security(oauth2_scheme)) -> dict:
    """Return current user from JWT token."""
    return decode_jwt_token(token)
