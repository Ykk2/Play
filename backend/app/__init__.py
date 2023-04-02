from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager


app = Flask(__name__, static_folder="../frontend/.next", static_url_path='/')


CORS(app)






login_manager = LoginManager(app)
login_manager.login_view = 'login'
