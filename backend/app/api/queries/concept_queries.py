from sqlalchemy.orm import joinload
from ...models import Concept, Figure


def find_concepts_name():
    concepts = Concept.query.all()
    return [concept.to_json_name_only for concept in concepts]


def find_concept_with_summary():
    concepts = Concept.query.all()
    return [concept.to_json_summary_only for concept in concepts]


def find_concept_with_explanation(concept_name):
    concept = Concept.query.filter_by(name=concept_name).options(
        joinload(Concept.figures)).order_by(Figure.order).first()
    return concept.to_json()
