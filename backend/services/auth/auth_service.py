from backend.repositories.users.user_repository import UserRepository
from backend.repositories.sessions.session_repository import SessionRepository
from backend.repositories.password_reset.password_reset_repository import PasswordResetRepository
from backend.models.users.user import User
from backend.models.sessions.session import Session
from backend.models.password_reset.password_reset import PasswordReset
from pydantic import EmailStr
from datetime import datetime, timedelta
import secrets

class AuthService:
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository, password_reset_repository: PasswordResetRepository):
        self.user_repository = user_repository
        self.session_repository = session_repository
        self.password_reset_repository = password_reset_repository

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

    def request_password_reset(self, email: EmailStr) -> PasswordReset:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise Exception('User with the provided email does not exist')
        reset_token = secrets.token_urlsafe(32)
        password_reset = PasswordReset(
            user_id=user.id,
            reset_token=reset_token,
            email=email,
            is_used=False,
            expires_at=datetime.now() + timedelta(hours=24),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.password_reset_repository.create_password_reset(password_reset)

    def verify_reset_token(self, token: str) -> Optional[PasswordReset]:
        password_reset = self.password_reset_repository.get_password_reset_by_token(token)
        if password_reset and password_reset.is_used:
            raise Exception('Password reset token has been used')
        if password_reset and password_reset.expires_at < datetime.now():
            raise Exception('Password reset token has expired')
        return password_reset

    def reset_password(self, token: str, new_password: str) -> User:
        password_reset = self.verify_reset_token(token)
        user = self.user_repository.get_user_by_id(password_reset.user_id)
        hashed_password = self._hash_password(new_password)
        user.password = hashed_password
        self.user_repository.update_user(user)
        self.password_reset_repository.mark_reset_as_used(password_reset.id)
        return user

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