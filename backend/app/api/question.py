from flask import Blueprint, request, jsonify
from ..models import User, db
from flask_login import login_required
from .helpers import format_errors



question_routes = Blueprint('questions', __name__)


@question_routes.route('/', methods=['GET'])
def get_questions():


    return "", 404
