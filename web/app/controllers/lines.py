from app.models.target_key import TargetKey as key
from app.models.target_user import TargetUser
from app import db


def get_client_ip(request):
    try:
        if request.headers.getlist("X-Forwarded-For"):
            return request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
        else:
            return "NONE"
    except:
        return "EXCEPT"


def validate_client_id(client_id):
    if len(str(client_id)) > 0 and client_id is not None:
        try:
            return key.query.filter_by(key_value=client_id).first()
        except:
            return False


def get_user_by_key_id(self, key_id):
    return TargetUser.query.filter_by(key_id=key_id).first()


def create_user(email, password, key_id, ip_address):
    user = TargetUser(email=email,
                      password=password,
                      key_id=key_id,
                      ip_address=ip_address)
    db.session.add(user)
    try:
        db.session.commit()
        return user
    except:
        db.session.rollback()


def increment_key(self, key):
    key.count = key.count + 1
    self.update_db()


def increment_visit(self, key, ip_address):
    key.visit = key.visit + 1
    key.visit_ip_address = ip_address
    self.update_db()


def increment_clicks(self, key, ip_address):
    key.clicked = key.clicked + 1
    key.clicked_ip_address = ip_address
    self.update_db()


def increment_opened(self, key, ip_address):
    key.opened = key.opened + 1
    key.opened_ip_address = ip_address
    self.update_db()


def update_db():
    try:
        db.session.commit()
    except:
        db.session.rollback()
