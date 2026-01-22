from .db import create_db

def init_configs(app):
    create_db(app)