from sqlalchemy.orm import Session

class UserService:
    async def get_user_by_email(email: str, db: Session):
        pass

user_service = UserService()