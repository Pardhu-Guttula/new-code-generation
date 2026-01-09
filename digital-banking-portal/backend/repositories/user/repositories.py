from digital_banking_portal.backend.models.user.models import User
from digital_banking_portal.backend import db

class UserRepository:

    @staticmethod
    def add_user(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def update_user() -> None:
        db.session.commit()

    @staticmethod
    def delete_user(user: User) -> None:
        db.session.delete(user)
        db.session.commit()