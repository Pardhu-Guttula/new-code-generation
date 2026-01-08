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

    def get_user_by_email(self, email: str) -> Optional[User]:
        logger.info("Fetching user by email=%s", email)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, email, password, login_attempts, is_locked, last_login_at, created_at, updated_at FROM users WHERE email=?",
                (email,),
            )
            row = cursor.fetchone()
            return User(*row) if row else None

    def update_user_login_attempts(self, user_id: int, attempts: int) -> None:
        logger.info("Updating login attempts for user_id=%s", user_id)
        with self._get_connection() as conn:
            conn.execute(
                "UPDATE users SET login_attempts=?, is_locked=? WHERE id=?",
                (attempts, attempts >= 5, user_id),
            )

    def update_last_login(self, user_id: int) -> None:
        logger.info("Updating last login time for user_id=%s", user_id)
        with self._get_connection() as conn:
            conn.execute(
                "UPDATE users SET last_login_at=?, login_attempts=0 WHERE id=?",
                (datetime.now(), user_id),
            )