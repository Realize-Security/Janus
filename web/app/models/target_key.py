from app import db


class TargetKey(db.Model):
    __tablename__ = 'target_keys'

    id = db.Column(db.Integer, primary_key=True)
    key_value = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, default=0)
    clicked = db.Column(db.Integer, default=0)
    visit = db.Column(db.Integer, default=0)
    opened = db.Column(db.Integer, default=0)
    clicked_ip_address = db.Column(db.String(255), nullable=True)
    opened_ip_address = db.Column(db.String(255), nullable=True)
    visit_ip_address = db.Column(db.String(255), nullable=True)

    def __init__(self, key_value, count):
        self.key_value = key_value
        self.count = count
