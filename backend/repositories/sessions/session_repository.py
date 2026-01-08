from backend.models.sessions.session import Session
from typing import List, Optional

class SessionRepository:
    def get_session_by_id(self, session_id: int) -> Optional[Session]:
        pass  # Implement database retrieval logic here

    def get_sessions_by_user_id(self, user_id: int) -> List[Session]:
        pass  # Implement database retrieval logic here

    def create_session(self, session: Session) -> Session:
        pass  # Implement database creation logic here

    def update_session(self, session: Session) -> Session:
        pass  # Implement database update logic here

    def delete_session(self, session_id: int) -> None:
        pass  # Implement database deletion logic here

    def deactivate_session(self, session_id: int) -> None:
        pass  # Implement session deactivation logic here