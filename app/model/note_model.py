import uuid
from sqlalchemy import String, DateTime, func, Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class Notes(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now(), nullable=False)
    user_id = Column(UUID(as_uuid=UUID), ForeignKey("users.id"), nullable=False)

    user = relationship("Users", back_populates="notes")
