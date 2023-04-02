from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from .models import db, User
from .config import Config


app = Flask(__name__, static_folder="../frontend/.next", static_url_path='/')
app.config.from_object(Config)

CORS(app)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
