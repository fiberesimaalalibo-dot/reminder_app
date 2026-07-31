from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    username = Column(String(50), unique=True, index=True, nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    reminders = relationship("Reminder", back_populates="owner")


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(100), nullable=False)

    description = Column(String(300))

    due_date = Column(DateTime, nullable=False)

    priority = Column(String(20), nullable=False)

    status = Column(String(20), default="Pending")

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="reminders")
