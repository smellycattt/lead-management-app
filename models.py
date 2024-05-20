from sqlalchemy import Column, Integer, String, Enum
from database import Base
from enum import Enum as PyEnum

class LeadState(PyEnum):
    PENDING = "PENDING"
    REACHED_OUT = "REACHED_OUT"

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    resume = Column(String)
    state = Column(Enum(LeadState), default=LeadState.PENDING)
