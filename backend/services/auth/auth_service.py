from backend.repositories.users.user_repository import UserRepository
from backend.repositories.sessions.session_repository import SessionRepository
from backend.models.users.user import User
from backend.models.sessions.session import Session
from pydantic import EmailStr
from datetime import datetime, timedelta
import secrets

class AuthService:
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository):
        self.user_repository = user_repository
        self.session_repository = session_repository

    def register_user(self, email: EmailStr, password: str) -> User:
        # Hash the password before storing
        hashed_password = self._hash_password(password)
        user = User(email=email, password=hashed_password, created_at=datetime.now(), updated_at=datetime.now())
        return self.user_repository.create_user(user)

    def _hash_password(self, password: str) -> str:
        # Implement password hashing logic here
        pass

    def authenticate_user(self, email: EmailStr, password: str) -> Optional[Session]:
        user = self.user_repository.get_user_by_email(email)
        if user and self._verify_password(password, user.password):
            if user.is_locked:
                raise Exception('Account is locked due to too many failed login attempts')
            session_token = secrets.token_urlsafe(32)
            session = Session(
                user_id=user.id,
                session_token=session_token,
                is_active=True,
                expires_at=datetime.now() + timedelta(hours=1),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            return self.session_repository.create_session(session)
        return None

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        # Implement password verification logic here
        pass

    def increase_login_attempts(self, email: EmailStr) -> None:
        user = self.user_repository.get_user_by_email(email)
        if user:
            user.login_attempts += 1
            if user.login_attempts >= 5:
                user.is_locked = True
            self.user_repository.update_user(user)

    def reset_login_attempts(self, email: EmailStr) -> None:
        user = self.user_repository.get_user_by_email(email)
        if user:
            user.login_attempts = 0
            user.is_locked = False
            self.user_repository.update_user(user)