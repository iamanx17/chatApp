from pydantic import BaseModel
from utils.mongo import db


class followerEntity(BaseModel):
    follower_id: str


followerModel = db['followers']
