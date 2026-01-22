from backend.src.models.enums.AccountTypes import AccountTypes
from backend.src.models.enums.TransactionCategories import TransactionCategories
from ..config.db import db

class Bill(db.Model):
    __tablename__ = "bills"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(1000), nullable=True)
    due_date = db.Column(db.Date, nullable=False)
    payment_date = db.Column(db.Date, nullable=True)
    amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    category = db.Column(db.Enum(TransactionCategories, name="bill_category"), nullable=False)
    account_type = db.Column(db.Enum(AccountTypes, name="bill_account_type"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, description, due_date, amount, paid, category, account_type, user_id):
        self.description = description
        self.due_date = due_date
        self.amount = amount
        self.paid = paid
        self.category = category
        self.account_type = account_type
        self.user_id = user_id

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "due_date": self.due_date,
            "amount": self.amount,
            "paid": self.paid,
            "category": self.category,
            "account_type": self.account_type,
            "user_id": self.user_id
        }