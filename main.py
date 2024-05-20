from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models import Lead, LeadState
from schemas import LeadCreate, LeadUpdate, Lead as LeadSchema
from crud import create_lead as create_lead_crud, fetch_leads, update_lead_state
from database import SessionLocal, engine, get_db
from email_utils import send_email
from auth import get_current_username

# Create the database tables
Lead.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/leads/", response_model=LeadSchema)
async def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = create_lead_crud(db=db, lead=lead)
    await send_email(
        subject="New Lead Submitted",
        body=f"Lead details:\n\n{lead}",
        to=lead.email
    )
    await send_email(
        subject="New Lead Submitted",
        body=f"Lead details:\n\n{lead}",
        to="attorney@example.com"
    )
    return db_lead

@app.get("/leads/", response_model=List[LeadSchema])
def get_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    leads = fetch_leads(db=db, skip=skip, limit=limit)
    return leads

@app.put("/leads/{lead_id}", response_model=LeadSchema)
def update_lead(lead_id: int, lead_update: LeadUpdate, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    db_lead = update_lead_state(db=db, lead_id=lead_id, state=lead_update.state)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead
