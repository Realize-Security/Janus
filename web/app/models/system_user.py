from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def load_user(userid):
    return SystemUser.get(userid)


class SystemUser(db.Model, UserMixin):
    reg_key = db.relationship('RegKey', backref='RegKey', lazy='dynamic', uselist=False)
    reg_key_id = db.Column(db.Integer, db.ForeignKey('reg_keys.id'), nullable=True)

    __tablename__ = 'system_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Integer, nullable=False, default=0)
    

    def __init__(self, username, email, password, reg_key_id, is_active):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.reg_key_id = reg_key_id
        self.is_active = is_active

    
    def check_password(self, password):
        return check_password_hash(self.password, password)
