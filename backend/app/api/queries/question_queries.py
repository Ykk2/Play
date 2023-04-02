from flask_login import current_user
from ...models import Question, Concept, Bookmark
from ..services.elasticsearch.queries import search_questions


def find_question_by_id(id):
    """
    find a question by question id
    """
    question = Question.query.filter_by(id=id).first()
    if question:
        return question.to_json()
    else:
        return None


def find_question_by_name(name):
    """
    find a question with the given name with SQLAlchemy
    """
    question = Question.query.filter_by(name=name).first()
    if question:
        return question.to_json_preview()
    else:
        return None


def find_similar_questions(name):
    """
    find similar questions with the given name with Elasticsearch
    """
    questions = search_questions(name)
    if questions:
        return questions
    else:
        return None


def find_questions_by_difficulty(difficulty, page):
    """
    Looks for questions with given difficulty ("Basic", "Intermediate", "Advanced")
    """
    per_page = 20

    questions = Question.query.filter_by(
        difficulty=difficulty).paginate(page, per_page)

    if questions:
        return [question.to_json_preview() for question in questions]
    else:
        return None


def find_questions_by_concepts(concept, page):
    """
    Returns a list of questions with the given concepts
    """
    per_page = 20

    questions = Question.query.join(Question.concepts).filter(
                Concept.name == concept).paginate(page, per_page)

    if questions:
        return [question.to_json_preview() for question in questions]
    else:
        return None


def find_bookmarked_questions(user_id):
    """
    Returns a list of questions that the user has bookmarked
    """
    questions = Question.query.join(Bookmark).filter(
                Bookmark.user_id == user_id).all()

    if questions:
        return [question.to_json_preview() for question in questions]
    else:
        return None
