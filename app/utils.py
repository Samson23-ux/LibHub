from jose import jwt, JWTError
from passlib.context import CryptContext

import uuid
from typing import Optional
from datetime import datetime, timedelta

from app.core.config import settings
from app.schemas.auth import TokenData

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    data: TokenData, expire_time: Optional[timedelta] = None
) -> str:
    if expire_time:
        expire_time = datetime.now() + expire_time
    else:
        expire_time = datetime.now() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    payload = {
        'sub': data.sub,
        'exp': expire_time,
        'iat': datetime.now(),
    }

    token = jwt.encode(
        payload, settings.ACCESS_TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM
    )
    return token


def create_refresh_token(
    data: TokenData, expire_time: Optional[timedelta] = None
) -> tuple:
    if expire_time:
        expire_time = datetime.now() + expire_time
    else:
        expire_time = datetime.now() + timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )

    token_id = uuid.uuid4()
    payload = {
        'sub': data.sub,
        'exp': expire_time,
        'iat': datetime.now(),
        'jti': token_id,
    }

    token = jwt.encode(
        payload, settings.REFRESH_TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM
    )
    return token, token_id, expire_time


def decode_token(token: str, key: str) -> dict:
    try:
        payload = jwt.decode(token, key, algorithms=[settings.TOKEN_ALGORITHM])
        return payload
    except JWTError:
        return None
