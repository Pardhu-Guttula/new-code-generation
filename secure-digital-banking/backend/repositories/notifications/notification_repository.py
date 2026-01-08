from typing import Optional, List
from backend.models.notifications.notification import Notification

class NotificationRepository:
    def create(self, notification: Notification) -> Notification:
        # Dummy implementation; replace with actual database save logic
        pass

    def find_by_id(self, notification_id: int) -> Optional<Notification]:
        # Dummy implementation; replace with actual database query
        pass

    def find_by_user_id(self, user_id: int) -> List<Notification]:
        # Dummy implementation; replace with actual database query
        pass

    def mark_as_read(self, notification_id: int) -> None:
        # Dummy implementation; replace with actual database update logic
        pass

    def delete(self, notification_id: int) -> None:
        # Dummy implementation; replace with actual database delete logic
        pass