from flask import Flask
from .config.db import db
from .config import init_configs

def create_app(): 
    app =  Flask(__name__)
    init_configs(app)

    with app.app_context():
        db.create_all()

    return app