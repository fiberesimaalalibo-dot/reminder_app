# ==================================================
# Imports
# ==================================================

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


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


@app.get("/reminders")
def reminders(request: Request):
    return templates.TemplateResponse(request=request, name="reminders.html")
