from flask import Blueprint, request, jsonify
from backend.repositories.notifications.notification_repository import NotificationRepository
from backend.services.notifications.notification_service import NotificationService

notification_controller = Blueprint('notification_controller', __name__)
notification_repository = NotificationRepository()
notification_service = NotificationService(notification_repository)

@notification_controller.route('/notifications', methods=['POST'])
def create_notification():
    json_data = request.json
    user_id = json_data.get('user_id')
    type = json_data.get('type')
    message = json_data.get('message')

    notification = notification_service.create_notification(user_id, type, message)
    return jsonify(notification.dict()), 201

@notification_controller.route('/notifications/user/<int:user_id>', methods=['GET'])
def get_user_notifications(user_id: int):
    notifications = notification_service.get_user_notifications(user_id)
    return jsonify([notification.dict() for notification in notifications]), 200

@notification_controller.route('/notifications/<int:notification_id>/read', methods=['PUT'])
def mark_notification_as_read(notification_id: int):
    notification_service.mark_notification_as_read(notification_id)
    return jsonify({'message': 'Notification marked as read successfully'}), 200

@notification_controller.route('/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id: int):
    notification_service.delete_notification(notification_id)
    return jsonify({'message': 'Notification deleted successfully'}), 200