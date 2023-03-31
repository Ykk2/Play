from .db import db

class Concept(db.Model):
    __tablename__ = "concepts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    summary = db.Column(db.String(500), nullable=False)
    explanation = db.Column(db.Text, nullable=False)

    figures = db.relationship("Figure", back_populates="Concept", cascade="all, delete")
    questions = db.relationship("Question", secondary="question_concept_association", back_populates="concepts")

    def to_json(self):
        return {key: value for key, value in vars(self).items()}

    def to_json_summary(self):
        keys = ["explanation"]
        return {key: value for key, value in vars(self).items() if key not in keys}
