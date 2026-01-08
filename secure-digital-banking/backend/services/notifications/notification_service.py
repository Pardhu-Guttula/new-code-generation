from typing import List
from backend.models.notifications.notification import Notification
from backend.repositories.notifications.notification_repository import NotificationRepository

class NotificationService:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def create_notification(self, user_id: int, type: str, message: str) -> Notification:
        notification = Notification(user_id=user_id, type=type, message=message)
        return self.notification_repository.create(notification)

    def get_user_notifications(self, user_id: int) -> List<Notification]:
        return self.notification_repository.find_by_user_id(user_id)

    def mark_notification_as_read(self, notification_id: int) -> None:
        self.notification_repository.mark_as_read(notification_id)

    def delete_notification(self, notification_id: int) -> None:
        self.notification_repository.delete(notification_id)