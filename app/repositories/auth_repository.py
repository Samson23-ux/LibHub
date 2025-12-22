from sqlalchemy.orm import Session

from uuid import UUID
from app.models.users import RefreshToken

class AuthRepo:
    async def store_refresh_token(token: RefreshToken, db: Session):
        db.add(token)
        db.flush()
        db.refresh(token)

    async def get_refresh_token(token_id: UUID, db: Session) -> RefreshToken:
        refresh_token = db.query(RefreshToken).filter(RefreshToken.id == str(token_id)).first()
        return refresh_token

    async def update_refresh_token(token: RefreshToken, db: Session):
        db.add(token)
        db.flush()
        db.refresh(token)

auth_repo = AuthRepo()
