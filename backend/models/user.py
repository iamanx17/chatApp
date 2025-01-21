from pydantic import BaseModel, EmailStr
from typing import Optional
from utils.mongo import db


class userRegisterEntity(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    password: str


class userLoginEntity(BaseModel):
    email: EmailStr
    password: str


userModel = db['users']
