from pydantic import BaseModel, EmailStr, field_validator
from typing import Literal
from constants import SPEAKER_TYPE, GENERAL_TYPE, COMMUNITY_TYPE


class Participant(BaseModel):
    id: str
    ticket_type: Literal[SPEAKER_TYPE, GENERAL_TYPE, COMMUNITY_TYPE] # type: ignore
    name: str
    email: EmailStr
    phone: str

    @field_validator('phone')
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        if len(v) != 10:
            raise ValueError('Phone number must be exactly 10 digits')
        return v

