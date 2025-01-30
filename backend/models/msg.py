from pydantic import BaseModel, Field
from utils.mongo import db
from typing import Optional
from datetime import datetime

class messageEntity(BaseModel):
    message: str
    reciever_id: str
    user_id: str
    timestamp: Optional[datetime] = Field(created_at = datetime.utcnow())


msgModel = db['messages']