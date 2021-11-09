from app import db, login_manager


@login_manager.user_loader
def load_user(userid):
    return TargetUser.get(userid)


# TODO: Track user agents and OS
class TargetUser(db.Model):
    target_token = db.relationship('TargetToken', backref='TargetKey', lazy='dynamic', uselist=False)
    token_id = db.Column(db.Integer, db.ForeignKey('target_token.id'), nullable=True)

    __tablename__ = 'target_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=False)
    password = db.Column(db.String(255), nullable=True)
    ip_address = db.Column(db.String(255), nullable=True)

    def __init__(self, email, password, token_id, ip_address):
        self.email = email
        self.password = password
        self.token_id = token_id
        self.ip_address = ip_address
