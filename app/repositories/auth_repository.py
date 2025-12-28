from uuid import UUID
from sqlalchemy.orm import Session

from app.models.users import User
from app.models.users import RefreshToken

class AuthRepo:
    async def add_refresh_token(token: RefreshToken, db: Session):
        # store and update refresh token
        db.add(token)
        db.flush()
        db.refresh(token)

    async def get_refresh_token(token_id: UUID, db: Session) -> RefreshToken:
        refresh_token = db.query(RefreshToken).filter(RefreshToken.id == str(token_id)).first()
        return refresh_token

    async def update_password(user: User, db: Session):
        db.add(user)
        db.flush()
        db.refresh(user)

auth_repo = AuthRepo()
