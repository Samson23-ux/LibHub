from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.utils import decode_token
from app.core.config import settings
from app.schemas.users import UserInDBV1
from app.services.users import user_service
from app.database.session import SessionLocal
from app.errors import AuthenticationError, AuthorizationError

ouath2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(ouath2_scheme)
):
    payload = decode_token(token, settings.ACCESS_TOKEN_SECRET_KEY)

    if not payload:
        raise AuthenticationError()

    user = await user_service.get_user_by_email(payload.get('sub'), db)
    return user


async def required_role(role: str):
    def role_checker(user: UserInDBV1 = Depends(get_current_user)):
        if user.role != role:
            raise AuthorizationError()
        return user

    return role_checker
