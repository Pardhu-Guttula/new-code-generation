from typing import List
from backend.models.audit.audit_log import AuditLog
from backend.repositories.audit.audit_log_repository import AuditLogRepository

class AuditLogService:
    def __init__(self, audit_log_repository: AuditLogRepository):
        self.audit_log_repository = audit_log_repository

    def create_audit_log(self, user_id: int, action: str, details: str) -> AuditLog:
        audit_log = AuditLog(user_id=user_id, action=action, details=details)
        return self.audit_log_repository.save(audit_log)

    def get_audit_logs(self) -> List<AuditLog]:
        return self.audit_log_repository.find_all()

    def get_user_audit_logs(self, user_id: int) -> List<AuditLog]:
        return self.audit_log_repository.find_by_user_id(user_id)