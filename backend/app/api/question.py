from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from .queries import *



question_routes = Blueprint('questions', __name__)


@question_routes.route('/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id):

    result = find_question_by_id(question_id)

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404


@question_routes.route('/name/<string:question_name>', methods=['GET'])
def get_question_by_name(question_name):
    """
    Returns the question if found, if not returns a list of similar questions.
    """
    try:
        result = find_question_by_name(question_name)
        if result:
            return jsonify(result), 200
        else:
            try:
                result = find_similar_questions(question_name)
                return jsonify(result), 200
            except Exception as e:
                return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 400
    except Exception as e:
        return jsonify({'error': "Sorry, there seems to be something wrong with our servers."}), 503


@question_routes.route('/difficulty/<string:difficulty>', methods=['GET'])
def get_questions_by_difficulty(difficulty):
    try:
        result = find_questions_by_difficulty(difficulty)
        if result:
            return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404


@question_routes.route('/concept/<string:concept_name>', methods=['GET'])
def get_all_questions(concept_name):
    try:
        result = find_questions_by_concepts(concept_name)
        if result:
            return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404


@question_routes.route('/bookmarked', methods=['GET'])
@login_required
def get_questions_bookmarked():
    user_id = current_user.id
    try:
        result = find_bookmarked_questions(user_id)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404
    except Exception as e:
        return jsonify({'error': "Sorry, there seems to be something wrong with our servers."}), 503
