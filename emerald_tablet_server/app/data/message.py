from pydantic import BaseModel
from data import DataType, Content, MetaInfo, Location
from datetime import datetime
from fastapi import  Field
from zoneinfo import ZoneInfo


class Message(BaseModel):
    data_type: DataType = Field(DataType.MESSAGE, description="현재 데이터 종류")
    created_at: datetime = Field(default_factory=datetime.now(ZoneInfo("Asia/Seoul")), description="생성 시간")
    modified_at: datetime = Field(default_factory=datetime.now(ZoneInfo("Asia/Seoul")), description="수정 시간")
    content: Content  = Field(...,description="메시지 내용")
    meta: MetaInfo = Field(...,description="메시지 메타 정보")
    location: Location = Field(...,description="메시지 위치 정보")
    
