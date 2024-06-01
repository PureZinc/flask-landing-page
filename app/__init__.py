from .models import db
from .email import mail
from config import config, prod_config
from flask import Flask


def create_app(production=False):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    conf = config
    if production:
        conf = prod_config
    
    app.config.update(conf)
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
