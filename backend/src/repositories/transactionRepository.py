from ..models.Transaction import Transaction
from ..config.db import db

def list_all_transactions_from_user(user_id):
    return db.session.query(Transaction).filter(Transaction.user_id == user_id).all()

def find_transaction_by_id(transaction_id):
    return db.session.query(Transaction).filter(Transaction.id == transaction_id).first()


