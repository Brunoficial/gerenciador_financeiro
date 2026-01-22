from backend.src.models.enums.AccountTypes import AccountTypes
from backend.src.models.enums.TransactionCategories import TransactionCategories
from backend.src.models.enums.TransactionTypes import TransactionTypes
from ..config.db import db 

class Transaction (db.Model): 
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    description = db.Column(db.String(1000), nullable=True)
    date = db.Column(db.Date)
    value = db.Column(db.Float, nullable=False)
    type = db.Column(db.Enum(TransactionTypes, name="transaction_type"), nullable=False)
    category = db.Column(db.Enum(TransactionCategories, name="transaction_category"), nullable=False)
    account_type = db.Column(db.Enum(AccountTypes, name="account_type"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, description, date, value, type, category, account_type, user_id):
        self.description = description
        self.date = date
        self.value = value
        self.type = type
        self.category = category
        self.account_type = account_type
        self.user_id = user_id

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "date": self.date,
            "value": self.value,
            "type": self.type,
            "category": self.category,
            "account_type": self.account_type,
            "user_id": self.user_id
        }