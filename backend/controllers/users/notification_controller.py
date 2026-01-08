from flask import Blueprint, jsonify, request
from backend.services.notification_service import NotificationService
from backend.repositories.notification_repository import NotificationRepository

notification_controller = Blueprint('notification_controller', __name__)
notification_repository = NotificationRepository()
notification_service = NotificationService(notification_repository)

@notification_controller.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')
    
    if not user_id or not message:
        return jsonify({'message': 'User ID and message are required'}), 400
    
    notification = notification_service.send_notification(user_id, message)
    return jsonify(notification.dict()), 201

@notification_controller.route('/notifications', methods=['GET'])
def get_notifications():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    
    notifications = notification_service.get_notifications_for_user(int(user_id))
    return jsonify([notification.dict() for notification in notifications]), 200