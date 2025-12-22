import enum
from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    sub: EmailStr
