from typing import List
from backend.models.audit.audit import Audit
from backend.repositories.audit.audit_repository import AuditRepository

class AuditService:
    def __init__(self, audit_repository: AuditRepository):
        self.audit_repository = audit_repository

    def log_action(self, user_id: int, action: str, details: str) -> Audit:
        audit = Audit(user_id=user_id, action=action, details=details)
        return self.audit_repository.create(audit)

    def get_user_audit_log(self, user_id: int) -> List<Audit]:
        return self.audit_repository.find_by_user_id(user_id)