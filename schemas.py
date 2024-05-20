from pydantic import BaseModel, EmailStr
from enum import Enum

class LeadState(str, Enum):
    PENDING = "PENDING"
    REACHED_OUT = "REACHED_OUT"

class LeadBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    resume: str

class LeadCreate(LeadBase):
    pass

class LeadUpdate(BaseModel):
    state: LeadState

class Lead(LeadBase):
    id: int
    state: LeadState

    class Config:
        from_attributes = True  
