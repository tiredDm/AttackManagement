# 3rd-party packages
from flask import Flask, render_template, request, redirect, url_for
from flask_ngrok import run_with_ngrok
from flask_mongoengine import MongoEngine
from flask_talisman import Talisman
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from waitress import serve


# stdlib
from datetime import datetime
import os

# local
#from .client import MovieClient


db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()
#movie_client = MovieClient(os.environ.get("OMDB_API_KEY"))

#from .routes import main
from .users.routes import users
from .attacks.routes import attacks

def page_not_found(e):
    return render_template("404.html"), 404


def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/html"),('Content-Length', str(len(self.html)))])

        return [self.html]

def create_app(test_config=None):
    app = Flask(__name__)
    run_with_ngrok(app)
    Talisman(app)

    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

 #   app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(attacks)
    app.register_error_handler(404, page_not_found)

    login_manager.login_view = "users.login"


    return app
