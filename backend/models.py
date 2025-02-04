from pydantic import BaseModel, EmailStr, Field
from utils.mongo import db
from typing import Optional
from datetime import datetime

class MessageEntity(BaseModel):
    message: str
    reciever_id: str
    user_id: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)


class UserRegisterEntity(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    password: str


class UserLoginEntity(BaseModel):
    email: EmailStr
    password: str


userModel = db['users']
msgModel = db['messages']
followerModel = db['followers']