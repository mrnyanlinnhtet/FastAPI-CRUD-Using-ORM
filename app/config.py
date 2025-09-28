import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
    """Get Database URL."""
    DATABASE_URL = os.getenv("DB_URL")