from sqlalchemy.orm import Session
from models import Lead, LeadState
from schemas import LeadCreate, LeadUpdate

def create_lead(db: Session, lead: LeadCreate):
    db_lead = Lead(
        first_name=lead.first_name,
        last_name=lead.last_name,
        email=lead.email,
        resume=lead.resume,
        state=LeadState.PENDING,
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def fetch_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Lead).offset(skip).limit(limit).all()

def update_lead_state(db: Session, lead_id: int, state: LeadState):
    db_lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if db_lead:
        db_lead.state = state
        db.commit()
        db.refresh(db_lead)
    return db_lead
