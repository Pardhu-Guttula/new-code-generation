from flask import Blueprint, request, jsonify
from backend.repositories.audit.audit_repository import AuditRepository
from backend.services.audit.audit_service import AuditService

audit_controller = Blueprint('audit_controller', __name__)
audit_repository = AuditRepository()
audit_service = AuditService(audit_repository)

@audit_controller.route('/audit/log', methods=['POST'])
def log_action():
    json_data = request.json
    user_id = json_data.get('user_id')
    action = json_data.get('action')
    details = json_data.get('details')

    audit = audit_service.log_action(user_id, action, details)
    return jsonify(audit.dict()), 201

@audit_controller.route('/audit/user/<int:user_id>', methods=['GET'])
def get_user_audit_log(user_id: int):
    audit_log = audit_service.get_user_audit_log(user_id)
    return jsonify([audit.dict() for audit in audit_log]), 200