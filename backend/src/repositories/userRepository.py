from ..models.User import User
from ..config.db import db

def list_all_users():
    return db.session.query(User).all()

def find_user_by_id(user_id):
    return db.session.query(User).filter(User.id == user_id).first()

