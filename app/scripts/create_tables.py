# app/scripts/create_tables.py
import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from database import Base, engine

from model.user_model import Users
from model.note_model import Notes

__all__ = ["Users", "Notes"]


async def create_tables():
    """Create tables in the database."""
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def main():
    """Main Method"""
    try:
        print("Creating tables...")
        await create_tables()
        print("Tables created successfully!")
    except Exception as e:
        print("Error creating tables:", e)

if __name__ == "__main__":
    asyncio.run(main())
