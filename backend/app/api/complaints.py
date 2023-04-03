from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from .queries import *


"""
TO DO:
build out forms and finish routes after
Implement auto reply to user for initial reply
"""

complaint_routes = Blueprint('complaints', __name__)


@complaint_routes.route('/complaints', methods=['POST'])
@login_required
def get_all_complaints():
    return ""
