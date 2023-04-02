from .db import db, add_prefix_for_prod
from datetime import datetime

class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("questions.id")), nullable=False)
    bookmarked_at = db.Column(db.DateTime, default=datetime.utcnow)

    question = db.relationship("Question", back_populates="bookmarks")
    user = db.relationship("User", back_populates="bookmarks")

    def to_json(self):
        keys = ["user_id"]
        return {key: value for key, value in vars(self).items() if key not in keys}
