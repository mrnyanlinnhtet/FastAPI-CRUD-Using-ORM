from fastapi import FastAPI, Depends
from app.controller.user_controller import routers as user_routers
from app.controller.note_controller import routers as note_routers
from app.utils.authentication import get_current_user

app = FastAPI()

app.include_router(user_routers)
app.include_router(note_routers, dependencies=[Depends(get_current_user)])
