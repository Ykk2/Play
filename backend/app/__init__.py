from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from .models import db, User
from .config import Config

# initialize flask app
app = Flask(__name__, static_folder="../frontend/.next", static_url_path='/')

# configure app (env varibles, custom configs, etc)
app.config.from_object(Config)

# enable cors for security
CORS(app)

# import SQLAlchemy to flask app
db.init_app(app)

# integrate flask_migrate to app and db instance to give access to migration methods
Migrate(app, db)


login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
