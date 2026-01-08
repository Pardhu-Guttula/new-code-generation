import sqlite3
from datetime import datetime
from typing import Optional
from backend.models.users.user import User, PasswordReset
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

    def create_password_reset_token(self, user_id: int, token: str, expires_at: datetime) -> PasswordReset:
        logger.info("Creating password reset token for user_id=%s", user_id)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO password_resets (user_id, token, expires_at, created_at) VALUES (?, ?, ?, ?)",
                (user_id, token, expires_at, datetime.now()),
            )
            reset_id = cursor.lastrowid
        return PasswordReset(id=reset_id, user_id=user_id, token=token, expires_at=expires_at, created_at=datetime.now())

    def get_password_reset_by_token(self, token: str) -> Optional[PasswordReset]:
        logger.info("Fetching password reset token")
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, user_id, token, expires_at, created_at FROM password_resets WHERE token=?",
                (token,),
            )
            row = cursor.fetchone()
            return PasswordReset(*row) if row else None

    def update_user_password(self, user_id: int, new_password: str) -> None:
        logger.info("Updating password for user_id=%s", user_id)
        with self._get_connection() as conn:
            conn.execute(
                "UPDATE users SET password=?, updated_at=? WHERE id=?",
                (new_password, datetime.now(), user_id),
            )