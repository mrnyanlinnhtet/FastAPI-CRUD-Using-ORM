from fastapi import FastAPI
from app.controller.user_controller import routers

app = FastAPI()

app.include_router(routers)