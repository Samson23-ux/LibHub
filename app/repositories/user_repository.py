from uuid import UUID
from app.schemas.users import UserV1, UserCreateV1, UserUpdateV1

class UserRepo:
    async def get_users(
            sort: str | None = None,
            offset: int = 0,
            limit: int = 0
    ) -> list[UserV1]:
        pass


    async def get_user(user_id: UUID) -> UserV1:
        pass


    async def create_user(user_create: UserCreateV1) -> UserV1:
        pass


    async def update_user(user_update: UserUpdateV1, user_id: UUID) -> UserV1:
        pass


    async def delete_user(user_id: UUID):
        pass

user_repo = UserRepo()