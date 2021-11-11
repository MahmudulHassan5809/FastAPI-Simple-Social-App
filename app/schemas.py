from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from pydantic.networks import EmailStr
from pydantic.types import conint

from app.database import Base


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True



class UserLogin(BaseModel):
    email : EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str]

class PostBase(BaseModel):
    title : str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    title : Optional[str]
    content: Optional[str]
    published: Optional[bool]



class PostResponse(BaseModel):
    id: int
    title : str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)