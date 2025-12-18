from uuid import UUID
from app.schemas.authors import (
    AuthorV1,
    AuthorCreateV1,
    AuthorUpdateV1
)

class AuthorRepo:
    async def get_authors_v1(
            sort: str | None = None,
            offset: int = 0,
            limit: int = 0
    ) -> list[AuthorV1]:
        pass

    async def get_author_v1(author_id: UUID) -> AuthorV1:
        pass

    async def create_author_v1(author_create: AuthorCreateV1) -> AuthorV1:
        pass

    async def update_author_v1(author_id: UUID, author_update: AuthorUpdateV1) -> AuthorV1:
        pass

    async def delete_author_v1(author_id: UUID):
        pass

author_repo = AuthorRepo()