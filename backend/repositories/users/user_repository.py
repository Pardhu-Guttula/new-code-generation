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
                "SELECT id, email, password, first_name, last_name, phone_number, login_attempts, is_locked, last_login_at, created_at, updated_at FROM users WHERE email=?",
                (email,),
            )
            row = cursor.fetchone()
            return User(*row) if row else None

    def update_user_profile(self, user_id: int, first_name: str, last_name: str, phone_number: str) -> None:
        logger.info("Updating profile for user_id=%s", user_id)
        with self._get_connection() as conn:
            conn.execute(
                "UPDATE users SET first_name=?, last_name=?, phone_number=?, updated_at=? WHERE id=?",
                (first_name, last_name, phone_number, datetime.now(), user_id),
            )

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        logger.info("Fetching user by id=%s", user_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, email, password, first_name, last_name, phone_number, login_attempts, is_locked, last_login_at, created_at, updated_at FROM users WHERE id=?",
                (user_id,),
            )
            row = cursor.fetchone()
            return User(*row) if row else None