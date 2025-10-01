from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime


class CreateNote(BaseModel):
    title: str
    content: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    user_id: Optional[UUID4] = None

class UpdateNote(BaseModel):
    title: Optional[str] = ''
    content: Optional[str] = ''
    updated_at: Optional[datetime] = datetime.now()


class ResponseNote(BaseModel):
    id: UUID4
    title: str
    content: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    user_id: str


class ResponseNoteMessage(BaseModel):
    message: str
