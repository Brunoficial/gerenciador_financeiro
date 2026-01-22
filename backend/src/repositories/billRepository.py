from ..models.Bill import Bill 
from ..config.db import db 

def list_bills_from_user(user_id):
    return db.session.query(Bill).filter(Bill.user_id == user_id).all()

def find_bill_by_id(bill_id):
    return db.session.query(Bill).filter(Bill.id == bill_id).first()
