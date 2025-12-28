from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.errors import UserNotFound
from app.repositories.user_repository import user_repo

class UserService:
    async def get_user_by_email(email: str, db: Session):
        pass

    async def get_user_by_id(id: str, db: Session):
        user = user_repo.get_user_by_id(id, db)
        
        if not user:
            raise UserNotFound()

        return jsonable_encoder(user)

user_service = UserService()