from .db import db

question_concept_association = db.Table(
    "question_concept_association",
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id")),
    db.Column("concept_id", db.Integer, db.ForeignKey("concepts.id")),
)
