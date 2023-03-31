from .db import db, add_prefix_for_prod

class Figure(db.Model):
    __tablename__ = "figures"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(40), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("concepts.id")))
    order = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String(100), nullable=False)

    concept = db.relationship("Concept", back_populates="Figure")

    def to_json(self):
        keys = ["id", "order", "concept_id"]
        return {key: value for key, value in vars(self).items() if key not in keys}
