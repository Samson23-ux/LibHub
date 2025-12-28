from uuid import UUID
from sqlalchemy.orm import Session

from app.models.users import User, Role


class UserRepo:
    async def get_users(
        sort: str | None = None, offset: int = 0, limit: int = 0
    ) -> list[User]:
        pass

    async def get_user_by_id(user_id: UUID, db: Session) -> User:
        user = db.query(User).filter(User.id == user_id)
        return user

    async def get_user_by_email(email: str, db: Session) -> User:
        user = db.query(User).filter(email == User.email).first()
        return user

    async def get_role_id(user_role: str, db: Session) -> str:
        role = db.query(Role).filter(user_role == Role.name)
        return role.id

    async def create_user(user: User, db: Session):
        db.add(user)
        db.flush()
        db.refresh(user)

    async def update_user(user: User, db: Session):
        db.add(user)
        db.flush()
        db.refresh(user)

    async def delete_user(db: Session):
        pass


user_repo = UserRepo()
