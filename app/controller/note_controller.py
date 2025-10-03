from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.note_schemas import CreateNote, UpdateNote, ResponseNote, ResponseNoteMessage
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.authentication import get_current_user
from app.service import note_service

router = APIRouter(prefix="/notes")


@router.post("/", response_model=ResponseNoteMessage)
async def create_note_api(note: CreateNote, db: AsyncSession=Depends(get_db), user=Depends(get_current_user)):
    """Handle note creation."""
    note_object = note.model_dump()
    note_object["user_id"] = user["id"]
    await note_service.create_note(db, note_object)
    return {"message": " Note successfully created."}


@router.get("/", response_model=List[ResponseNote])
async def get_all_notes_api(db: AsyncSession=Depends(get_db), user=Depends(get_current_user)):
    """Handle get all notes."""
    user_id = user["id"]
    notes = await note_service.get_notes(db, user_id)

    if notes:
        return notes
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="[Controller]: Note note found!")


@router.get("/{note_id}", response_model=ResponseNote)
async def get_note_by_id_api(note_id: str, db: AsyncSession=Depends(get_db), user=Depends(get_current_user)):
    """Handle get note by note id."""
    user_id = user["id"]
    note_obj = await note_service.get_note_by_id(db, note_id, user_id)

    if note_obj:
        return note_obj
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="[Controller]: Note note found!")


@router.put("/{note_id}", response_model=ResponseNote)
async def update_note_api(note_id: str, note: UpdateNote, db: AsyncSession=Depends(get_db), user=Depends(get_current_user)):
    """Handle update note by note id."""
    user_id = user["id"]
    note_obj = await note_service.update_note(db, note_id, note, user_id)

    if note_obj:
        return note_obj
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="[Controller]: Note not found!")


@router.delete("/{note_id}", response_model=ResponseNote)
async def delete_note_api(note_id: str, db: AsyncSession=Depends(get_db), user=Depends(get_current_user)):
    """Handle delete note by note id."""
    user_id = user["id"]
    note_obj = await note_service.delete_note(db, note_id, user_id)

    if note_obj:
        return note_obj
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="[Controller]: Note not found!")
