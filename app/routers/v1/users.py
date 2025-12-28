from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import APIRouter, Query, Depends

from app.models.users import User
from app.dependencies import get_db, get_current_user
from app.schemas.users import UserUpdateV1, Response

users_router_v1 = APIRouter()


@users_router_v1.get('/users/', status_code=200, response_model=Response)
async def get_users(
    sort: str = Query(...),
    offset: int = Query(...),
    limit: int = Query(...),
    db: Session = Depends(get_db),
):
    pass


@users_router_v1.get('/users/{user_id}/', status_code=200, response_model=Response)
async def get_user(
    user_id: UUID, user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    pass


@users_router_v1.patch('/users/{user_id}/', status_code=200, response_model=Response)
async def update_user(
    user_id: UUID, user_update: UserUpdateV1, db: Session = Depends(get_db)
):
    pass


@users_router_v1.delete('/users/{user_id}/', status_code=204)
async def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    pass
