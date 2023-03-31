from .db import db
from sqlalchemy import Enum


ALLOWED_DIFFICULTY = ["Basic", "Intermediate", "Advanced"]


class QuestionType(Enum):
    __values__ = ALLOWED_DIFFICULTY


class Question(db.model):
    _tablename_ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    difficulty = db.Column(QuestionType, nullable=False)
    body = db.Column(db.Text, nullable=False)
    video = db.Column(db.String(500), nullable=False, unique=True)
    explanation = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {key: value for key, value in self.__dict__.items()}
