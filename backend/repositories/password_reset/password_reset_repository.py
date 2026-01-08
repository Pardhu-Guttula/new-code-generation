from backend.models.password_reset.password_reset import PasswordReset
from typing import Optional

class PasswordResetRepository:
    def get_password_reset_by_id(self, reset_id: int) -> Optional[PasswordReset]:
        pass  # Implement database retrieval logic here

    def get_password_reset_by_email(self, email: str) -> Optional[PasswordReset]:
        pass  # Implement database retrieval logic here

    def create_password_reset(self, password_reset: PasswordReset) -> PasswordReset:
        pass  # Implement database creation logic here

    def update_password_reset(self, password_reset: PasswordReset) -> PasswordReset:
        pass  # Implement database update logic here

    def mark_reset_as_used(self, reset_id: int) -> None:
        pass  # Implement marking reset as used logic here