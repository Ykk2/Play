from flask import Blueprint, request, jsonify
from ..models import User, db
from flask_login import login_required
from .helpers import format_errors
from ...elasticsearch.search import search_questions

question_routes = Blueprint('auth', __name__)


@question_routes.route('/questions', methods=['GET'])
@login_required
def get_questions():
    return "", 404
