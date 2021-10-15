from sys import path
from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()

from .routes import routes as mainRouter
from .routes import auth as authRouter

from .config import Config

def createflaskapp():
    app = Flask(__name__)

    app.config.from_object(Config())
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(mainRouter.route)
    app.register_blueprint(authRouter.auth)
    
    return app
