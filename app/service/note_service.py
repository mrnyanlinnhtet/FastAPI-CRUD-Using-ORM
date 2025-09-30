from uuid import UUID
from app.schemas.note_schemas import CreateNote, UpdateNote
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.model.note_model import Notes
from fastapi import HTTPException, status


async def create_note(db: AsyncSession, note: CreateNote):
    """Create note."""
    note_object = Notes(**note.model_dump())
    db.add(note_object)
    await db.commit()
    await db.refresh(note_object)
    return note_object


async def get_note_by_id(db: AsyncSession, note_id: UUID):
    "Get note by note id."
    note_object = await db.execute(select(Notes).where(Notes.id == note_id))
    return note_object.scalar_one_or_none()


async def get_notes(db: AsyncSession):
    """Get all notes for specific user."""
    notes = await db.execute(select(Notes))
    return notes.scalars().all()


async def update_note(db: AsyncSession, note_id: UUID, note: UpdateNote):
    """Update note by note id."""
    data = await db.execute(select(Notes).where(note_id))
    note_object = data.scalar_one_or_none()

    if not note_object:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="[Service]: Note not found!")
    else:
        for key, value in note.model_dump(exclude_unset=True).items():
            setattr(note_object, key, value)
        await db.commit()
        await db.refresh(note_object)
        return note_object


async def delete_note(db: AsyncSession, note_id: UUID):
    """Delete note by note id."""
    note_obj = await db.execute(select(Notes).where(Notes.id == note_id))

    if not note_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="[Service]: Note not found!")
    else:
        await db.delete(note_obj)
        await db.commit()
        return note_obj
