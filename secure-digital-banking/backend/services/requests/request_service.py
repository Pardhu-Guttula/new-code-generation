from typing import List
from backend.models.requests.request import Request
from backend.repositories.requests.request_repository import RequestRepository

class RequestService:
    def __init__(self, request_repository: RequestRepository):
        self.request_repository = request_repository

    def create_request(self, user_id: int, type: str, details: str, status: str) -> Request:
        request = Request(user_id=user_id, type=type, details=details, status=status)
        return self.request_repository.create(request)

    def get_request(self, request_id: int) -> Request:
        return self.request_repository.find_by_id(request_id)

    def get_user_requests(self, user_id: int) -> List<Request]:
        return self.request_repository.find_by_user_id(user_id)

    def update_request(self, request: Request) -> Request:
        return self.request_repository.update(request)

    def delete_request(self, request_id: int) -> None:
        self.request_repository.delete(request_id)