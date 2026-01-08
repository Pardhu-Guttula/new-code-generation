import os

class Settings:
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "database/app.db")
    DEBUG: bool = bool(os.getenv("DEBUG", True))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")

settings = Settings()