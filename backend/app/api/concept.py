from flask import Blueprint, jsonify
from .queries import *

concept_routes = Blueprint('concepts', __name__)


@concept_routes.route('/', methods=['GET'])
def get_concepts_just_name():
    """
    Returns just name of all concepts.
    """
    result = find_concepts_by_name()
    try:
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@concept_routes.route('/summary', methods=['GET'])
def get_concepts_summary():
    """
    Returns concepts with summary.
    """
    try:
        result = find_concept_with_summary()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@concept_routes.route('/explanation', methods=['GET'])
def get_concept_explanation():
    """
    Returns a single concept with explanation
    """
    try:
        result = find_concept_with_explanation()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': "Sorry, we couldn't find what you were looking for."}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
