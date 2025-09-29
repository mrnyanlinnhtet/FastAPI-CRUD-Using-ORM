from uuid import UUID
from app.schemas.note_schemas import CreateNote, UpdateNote
from sqlalchemy.ext.asyncio import AsyncSession


async def create_note(db: AsyncSession, note: CreateNote):
    """Create note."""
    pass


async def get_note_by_id(db: AsyncSession, note_id: UUID):
    "Get note by note id."
    pass


async def get_notes(db: AsyncSession):
    """Get all notes for specific user."""
    pass


async def update_note(db: AsyncSession, note_id: UUID, note: UpdateNote):
    """Update note by note id."""
    pass


async def delete_note(db: AsyncSession, note_id: UUID):
    """Delete note by note id."""
    pass