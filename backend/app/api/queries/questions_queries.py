from ...models import Question
from ..services.elasticsearch.queries import search_questions


def get_questions_by_name(name):
    """
    First tries to find a question with the given name.
    If not found, use elasticsearch to find top matches.
    """
    question = Question.query.filter_by(name=name).first()

    if question:
        return question.to_json()
    else:
        question = search_questions(name)
        if question:
            return question
        else:
            return []


def get_questions_by_difficulty(difficulty):
    """
    Looks for questions with given difficulty ("Basic", "Intermediate", "Advanced")
    """
    questions = Question.query.filter_by(difficulty=difficulty).all()

    if questions:
        return [question.to_json() for question in questions]
    else:
        return []
