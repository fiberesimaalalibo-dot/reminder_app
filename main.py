# ==================================================
# Imports
# ==================================================

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


import models
from database import Base, engine, SessionLocal
from models import User


Base.metadata.create_all(bind=engine)

# ==================================================
# FastAPI Configuration
# ==================================================
app = FastAPI(
    title="Reminder App",
    description="A simple reminder app to manage tasks and deadlines.",
    version="1.0.0",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/register")
def register(request: Request):
    return templates.TemplateResponse(request=request, name="register.html")


@app.post("/register")
def register_user(
    full_name: str = Form(...),
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    db = SessionLocal()
    try:
        user = User(
            full_name=full_name, username=username, email=email, password=password
        )
        db.add(user)
        db.commit()
        return {"message": "Student registered successfully!"}
    finally:
        db.close()


@app.get("/reminders")
def reminders(request: Request):
    return templates.TemplateResponse(request=request, name="reminders.html")


@app.get("/dashboard", name="dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html")
