from enum import Enum 
from pydantic import BaseModel,field_validator
from typing import List
from fastapi import  Field

class DataType(str,Enum):
    MEMO = "memo"
    MESSAGE = "message"

class Tag(str,Enum):
    FESTIVAL = "festival"
    
class Grade(int,Enum):
    BEGINNER = 0
    INTERMEDIATE = 1
    ADVANCED = 3
    

LATITUDE_REGEX = (
    r'^('
    r'-?\d{1,2}\.\d+|'                          # DD
    r'\d{1,2}\s\d{1,2}\.\d+|'                   # DMM
    r'\d{1,2}°\d{1,2}\'\d{1,2}(\.\d+)?\"?[NS]'  # DMS
    r')$'
)

LONGITUDE_REGEX = (
    r'^('
    r'-?\d{1,3}\.\d+|'                          # DD
    r'\d{1,3}\s\d{1,2}\.\d+|'                   # DMM
    r'\d{1,3}°\d{1,2}\'\d{1,2}(\.\d+)?\"?[EW]'  # DMS
    r')$'
)

class Content(BaseModel):
    title: str = Field(None,description="메시지 제목 내용")
    content: str = Field(None,description="메시지 내용")
    image: str = Field(None,description="base64 이미지")

class MetaInfo(BaseModel):
    tag:List[Tag] = Field(None,description="테그")
    author: str = Field(...,description="작성자")
    grade: Grade = Field(...,description="신뢰 등급")
    
class Restriction(BaseModel):
    visiable: str = Field(None, description="메시지를 볼수 있는 대상 지정")
    min_distance: float = Field(None, description="메시지를 볼 수 있는 최소 거리")
    max_distance: float = Field(None, description="메시지를 볼 수 있는 최대 거리")

class Location(BaseModel):
    latitude: str = Field(..., pattern=LATITUDE_REGEX, description="위도: DD, DMM, 또는 DMS 형식")
    longitude: str = Field(..., pattern=LONGITUDE_REGEX, description="경도: DD, DMM, 또는 DMS 형식")
    address: str = Field(None, description="주소")
    
    @field_validator("latitude", "longitude")
    @classmethod
    def validate_dd_range(cls, v, info):
        try:
            num = float(v)
            if info.field_name == "latitude" and not (-90 <= num <= 90):
                raise ValueError("위도는 -90 ~ 90 사이여야 합니다.")
            if info.field_name == "longitude" and not (-180 <= num <= 180):
                raise ValueError("경도는 -180 ~ 180 사이여야 합니다.")
        except ValueError:
            pass  # DD 형식이 아닐 경우 float 변환 실패 → DMS, DMM 형식으로 간주
        return v