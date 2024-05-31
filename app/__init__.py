from .models import db
from .email import mail
from config import config
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    app.config.update(config)
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
