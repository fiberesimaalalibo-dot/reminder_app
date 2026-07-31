from datetime import datetime

from pydantic import BaseModel, EmailStr


# -------------------------
# User Schemas
# -------------------------


class UserCreate(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# -------------------------
# Reminder Schemas
# -------------------------


class ReminderCreate(BaseModel):
    title: str
    description: str
    due_date: datetime
    priority: str


class ReminderResponse(ReminderCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
