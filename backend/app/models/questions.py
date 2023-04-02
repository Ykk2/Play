from .db import db
from sqlalchemy import Enum

ALLOWED_DIFFICULTY = ["Basic", "Intermediate", "Advanced"]

class QuestionType(Enum):
    __values__ = ALLOWED_DIFFICULTY

class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    difficulty = db.Column(QuestionType, nullable=False)
    body = db.Column(db.Text, nullable=False)
    video = db.Column(db.String(500), nullable=False, unique=True)
    explanation = db.Column(db.Text, nullable=False)

    concepts = db.relationship("Concept", secondary="question_concept_association", back_populates="questions")

    def to_json(self):
        return {key: value for key, value in vars(self).items()}

    def to_json_preview(self):
        keys = ["video", "body", "explanation"]
        return {key: value for key, value in vars(self).items() if key not in keys}
