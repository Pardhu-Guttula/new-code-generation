from datetime import datetime
from digital_banking_portal.backend.models import db

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary key=True, autoincrement=True)
    action = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"AuditLog('{self.action}', 'User ID: {self.user_id}', 'Timestamp: {self.timestamp}')"