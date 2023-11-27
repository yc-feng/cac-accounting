from flask import Flask
from flask_login import LoginManager
from .models import User
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config') 

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
