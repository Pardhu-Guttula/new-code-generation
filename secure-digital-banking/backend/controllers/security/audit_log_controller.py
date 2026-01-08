from flask import Blueprint, request, jsonify
from backend.repositories.audit.audit_log_repository import AuditLogRepository
from backend.services.security.audit_log_service import AuditLogService

audit_log_controller = Blueprint('audit_log_controller', __name__)
audit_log_repository = AuditLogRepository()
audit_log_service = AuditLogService(audit_log_repository)

@audit_log_controller.route('/audit_logs', methods=['GET'])
def get_audit_logs():
    audit_logs = audit_log_service.get_audit_logs()
    return jsonify([audit_log.dict() for audit_log in audit_logs]), 200

@audit_log_controller.route('/audit_logs/<int:user_id>', methods=['GET'])
def get_user_audit_logs(user_id: int):
    audit_logs = audit_log_service.get_user_audit_logs(user_id)
    return jsonify([audit_log.dict() for audit_log in audit_logs]), 200