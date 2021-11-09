from app import db


class RegKey(db.Model):

    __tablename__ = 'reg_keys'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    reg_key = db.Column(db.String(70), nullable=False)
    

    def __init__(self, email, reg_key):
        self.email = email
        self.reg_key = reg_key
