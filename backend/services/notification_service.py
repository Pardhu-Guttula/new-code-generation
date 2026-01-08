from typing import List
from backend.models.notification import Notification
from backend.repositories.notification_repository import NotificationRepository

class NotificationService:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def send_notification(self, user_id: int, message: str) -> Notification:
        notification = Notification(user_id=user_id, message=message)
        return self.notification_repository.create(notification)

    def get_notifications_for_user(self, user_id: int) -> List[Notification]:
        return self.notification_repository.find_by_user_id(user_id)

    def update_notification_status(self, notification: Notification) -> Notification:
        return self.notification_repository.update(notification)