from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from .queries import *


bookmark_routes = Blueprint('concepts', __name__)


@bookmark_routes.route('/add/<int:question_id>', methods=['POST'])
@login_required
def add_to_bookmark(question_id):
    user_id = current_user.id
    try:
        result = add_bookmark(user_id, question_id)
        if (result):
            return "", 200
        else:
            return {'error': "Sorry, there seems to be an error. Please try reloading your browser."}, 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bookmark_routes.route('/remove/<int:bookmark_id>', methods=['POST'])
@login_required
def remove_from_bookmark(bookmark_id):
    try:
        result = remove_bookmark(bookmark_id)
        if (result):
            return "", 200
        else:
            return {'error': "Sorry, there seems to be an error. Please try reloading your browser."}, 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
