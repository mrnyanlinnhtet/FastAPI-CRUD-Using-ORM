from fastapi import FastAPI, Depends
from app.controller.user_controller import router as user_router
from app.controller.note_controller import router as note_router

app = FastAPI()

app.include_router(user_router)
app.include_router(note_router)
