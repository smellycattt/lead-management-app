from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
from models import Lead, LeadState
from schemas import LeadCreate, LeadUpdate, Lead as LeadSchema
from crud import create_lead as create_lead_crud, fetch_leads, update_lead_state
from database import SessionLocal, engine, get_db
from email_utils import send_email
from auth import get_current_username
import os
import shutil

# Create the database tables
Lead.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/leads/", response_model=LeadSchema)
async def create_lead(
    first_name: str,
    last_name: str,
    email: str,
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    resume_path = os.path.join(UPLOAD_DIR, resume.filename)
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
    
    lead_data = LeadCreate(first_name=first_name, last_name=last_name, email=email)
    db_lead = create_lead_crud(db=db, lead=lead_data, resume_path=resume_path)
    
    await send_email(
        subject="New Lead Submitted",
        body=f"Lead details:\n\n{lead_data}",
        to=email
    )
    await send_email(
        subject="New Lead Submitted",
        body=f"Lead details:\n\n{lead_data}",
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
