import os

class Settings:
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "database/app.db")
    DEBUG: bool = bool(os.getenv("DEBUG", True))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    PERMANENT_SESSION_LIFETIME: int = int(os.getenv("PERMANENT_SESSION_LIFETIME", 30 * 60))  # 30 minutes

settings = Settings()