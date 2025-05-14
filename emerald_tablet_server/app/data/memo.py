from pydantic import BaseModel
from fastapi import  Field
from data import Restriction
from data.message import Message

class Memo(BaseModel):
    message: Message = Field(...,description="메모 내용")
    restriction: Restriction = Field(...,description="메모 제약 조건")
    