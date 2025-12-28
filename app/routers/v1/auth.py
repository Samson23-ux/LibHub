from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Form, Response as re, Cookie

from app.models.users import User
from app.errors import ServerError
from app.services.auth import auth_service
from app.dependencies import get_db, get_current_user
from app.schemas.users import UserCreateV1, PasswordUpdate, Response


auth_router_v1 = APIRouter()


@auth_router_v1.post('/auth/signup/', status_code=201, response_model=Response)
async def sign_up(user_create: UserCreateV1, db: Session = Depends(get_db)):
    try:
        user = await auth_service.sign_up(user_create, db)
        db.commit()
        return Response(message='Sign up completed successfully', data=user)
    except Exception as e:
        db.rollback()
        raise ServerError from e


@auth_router_v1.post('/auth/sign-in/', status_code=201, response_model=Response)
async def sign_in(
    email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)
):
    try:
        data = await auth_service.sign_in(email, password, db)

        re.set_cookie(
            key='refresh_token', value=data.get('refresh_token'), httponly=True
        )

        return Response(
            message='Sign in completed successfully', data=data.get('access_token')
        )
    except Exception as e:
        db.rollback()
        raise ServerError() from e


@auth_router_v1.post('/auth/token/refresh/', status_code=201, response_model=Response)
async def create_new_token(
    #request for a new access token with a valid refresh token
    refresh_token: Optional[str] = Cookie(None),
    _=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        data = await auth_service.create_new_token(refresh_token, db)

        re.set_cookie(
            key='refresh_token', value=data.get('refresh_token'), httponly=True
        )

        return Response(
            message='Access token generated successfully', data=data.get('access_token')
        )
    except Exception as e:
        db.rollback()
        raise ServerError() from e


@auth_router_v1.patch('/auth/password_reset/', status_code=200, response_model=Response)
async def update_password(
    password_update: PasswordUpdate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        auth_service.update_password(password_update, user, db)
        return Response(message='Password updated successfully')
    except Exception as e:
        db.rollback()
        raise ServerError() from e


@auth_router_v1.patch('/auth/sign-out', status_code=200, response_model=Response)
async def sign_out(
    refresh_token: Optional[str] = Cookie(None),
    _=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        auth_service.sign_out(refresh_token, db)
        return Response(message='Sign out completed successfully')
    except Exception as e:
        db.rollback()
        raise ServerError() from e
