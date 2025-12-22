from sqlalchemy.orm import Session
from typing import Optional
from fastapi import APIRouter, Depends, Form, Response as re, Cookie

from app.dependencies import get_db
from app.errors import ServerError
from app.services.auth import auth_service
from app.schemas.users import UserCreateV1, Response


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
    refresh_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)
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


@auth_router_v1.patch('/auth/sign-out', status_code=200, response_model=Response)
async def sign_out(refresh_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    try:
        auth_service.sign_out(refresh_token, db)
        return Response(message='Sign out completed successfully')
    except Exception as e:
        db.rollback()
        raise ServerError() from e
