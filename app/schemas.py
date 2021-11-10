from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from pydantic.networks import EmailStr

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

    class Config:
        orm_mode = True


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