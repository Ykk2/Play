from .db import db, add_prefix_for_prod
from datetime import datetime

class Complaint(db.Model):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    origin = db.Column(db.String(100), nullable=False, default="general")
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="Complaint")

    def to_json(self):
        return {key: value for key, value in vars(self).items()}
