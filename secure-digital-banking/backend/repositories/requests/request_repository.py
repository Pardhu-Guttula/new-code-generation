from typing import Optional, List
from backend.models.requests.request import Request

class RequestRepository:
    def create(self, request: Request) -> Request:
        # Dummy implementation; replace with actual database save logic
        pass

    def find_by_id(self, request_id: int) -> Optional<Request]:
        # Dummy implementation; replace with actual database query
        pass

    def find_by_user_id(self, user_id: int) -> List<Request]:
        # Dummy implementation; replace with actual database query
        pass

    def update(self, request: Request) -> Request:
        # Dummy implementation; replace with actual database update logic
        pass

    def delete(self, request_id: int) -> None:
        # Dummy implementation; replace with actual database delete logic
        pass