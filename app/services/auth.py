from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.models.users import User
from app.utils import decode_token
from app.core.config import settings
from app.models.users import RefreshToken
from app.schemas.auth import TokenData, Token
from app.repositories.auth_repository import auth_repo
from app.repositories.user_repository import user_repo
from app.schemas.users import UserInDBV1, UserCreateV1, PasswordUpdate
from app.errors import UserExistError, EmailError, PasswordError, AuthenticationError
from app.utils import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)


class AuthService:
    async def sign_up(user_create: UserCreateV1, db: Session) -> UserInDBV1:
        if user_repo.get_user_by_email(user_create.email, db):
            raise UserExistError()

        role_id = await user_repo.get_role_id(user_create.role, db)

        user_create.password = hash_password(user_create.password)
        user_in_db = User(**user_create.model_dump(exclude={'role'}), role=role_id)

        user_repo.create_user(user_in_db, db)
        user = await user_repo.get_user_by_email(user_create.email, db)
        return jsonable_encoder(user, exclude={'password'})

    async def sign_in(email: str, password: str, db: Session):
        user = user_repo.get_user_by_email(email, db)
        if not user:
            raise EmailError()

        if not verify_password(password, user.password):
            raise PasswordError()

        token_data = TokenData(email=email)
        access_token = create_access_token(token_data)
        refresh_token, token_id, expire_time = create_refresh_token(token_data)

        db_token = RefreshToken(
            id=token_id, user_id=user.id, token=refresh_token, expires_at=expire_time
        )

        auth_repo.add_refresh_token(db_token, db)

        token = Token(token=access_token, token_type='Bearer')
        data = {'access_token': token, 'refresh_token': refresh_token}
        return data

    async def create_new_token(refresh_token: str, db: Session) -> str:
        payload = decode_token(refresh_token, settings.REFRESH_TOKEN_SECRET_KEY)
        if payload is None or refresh_token is None:
            raise AuthenticationError()

        db_refresh_token = await auth_repo.get_refresh_token(payload.get('jti'), db)

        if db_refresh_token.status == 'revoked':
            raise AuthenticationError()

        db_refresh_token.status = 'used'
        db_refresh_token.used_at = datetime.now()
        auth_repo.add_refresh_token(db_refresh_token, db) #update refresh token

        token_data = TokenData(email=payload.get('sub'))
        access_token = create_access_token(token_data)
        new_refresh_token, token_id, expire_time = create_refresh_token(token_data)

        new_db_refresh_token = RefreshToken(
            id=token_id, user_id=refresh_token.user_id, token=refresh_token, expires_at=expire_time
        )

        auth_repo.add_refresh_token(new_db_refresh_token, db)

        token = Token(token=access_token, token_type='Bearer')
        data = {'access_token': token, 'refresh_token': new_refresh_token}
        return data
    
    async def sign_out(refresh_token: str, db: Session):
        refresh_token = decode_token(refresh_token, settings.REFRESH_TOKEN_SECRET_KEY)

        refresh_token_db = await auth_repo.get_refresh_token(refresh_token.get('sub'), db)

        refresh_token_db.status = 'revoked'
        refresh_token_db.revoked_at = datetime.now()
        auth_repo.add_refresh_token(refresh_token_db, db)

    async def update_password(password_update: PasswordUpdate, user: User, db: Session):
        if not verify_password(password_update.old_password, user.password):
            raise PasswordError()
        
        user.password = hash_password(password_update.new_password)
        user_repo.update_user(user, db)


auth_service = AuthService()
