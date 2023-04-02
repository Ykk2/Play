from flask import Blueprint, request, jsonify
from flask_login import login_required
from .queries import *
from .helpers import format_errors, no_resource_error


question_routes = Blueprint('questions', __name__)


@question_routes.route('/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):

    result = find_question_by_id(question_id)

    if result:
        return jsonify(result), 200
    else:
        return jsonify(no_resource_error), 404


@question_routes.route('/<string:question_name>', methods=['GET'])
def get_question_by_name(question_name):
    try:
        result = find_question_by_name(question_name)
        if result:
            return jsonify(result), 200
        else:
            try:
                result = find_similar_questions(question_name)
                return jsonify(result), 200
            except Exception as e:
                return jsonify(format_errors(e)), 400
    except Exception as e:
        return jsonify(format_errors(e)), 400
