import sqlite3
from datetime import datetime
from typing import Optional
from backend.models.users.user import User
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self._db_path, detect_types=sqlite3.PARSE_DECLTYPES)

    def create_user(self, email: str, password: str) -> User:
        logger.info("Creating user with email=%s", email)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            created_at = datetime.now()
            cursor.execute(
                "INSERT INTO users (email, password, created_at, updated_at) VALUES (?, ?, ?, ?)",
                (email, password, created_at, created_at),
            )
            user_id = cursor.lastrowid
        return User(id=user_id, email=email, password=password, created_at=created_at, updated_at=created_at)

    def get_user_by_email(self, email: str) -> Optional[User]:
        logger.info("Fetching user by email=%s", email)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, email, password, created_at, updated_at FROM users WHERE email=?",
                (email,),
            )
            row = cursor.fetchone()
            return User(*row) if row else None