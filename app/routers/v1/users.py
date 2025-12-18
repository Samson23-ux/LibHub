from uuid import UUID
from fastapi import APIRouter, Query
from app.schemas.users import UserCreateV1, UserUpdateV1, Response

users_router_v1 = APIRouter()


@users_router_v1.get(
    '/users/',
    status_code=200,
    response_model=Response)
async def get_users(
    sort: str = Query(...),
    offset: int = Query(...),
    limit: int = Query(...)
):
    pass


@users_router_v1.get(
    '/users/{user_id}/',
    status_code=200,
    response_model=Response
)
async def get_user(user_id: UUID):
    pass


@users_router_v1.post(
    '/users/',
    status_code=201,
    response_model=Response
)
async def create_user(user_create: UserCreateV1):
    pass


@users_router_v1.patch(
    '/users/{user_id}/',
    status_code=200,
    response_model=Response
)
async def update_user(
    user_id: UUID,
    user_update: UserUpdateV1
):
    pass


@users_router_v1.delete(
    '/users/{user_id}/',
    status_code=204
)
async def delete_user(user_id: UUID):
    pass
