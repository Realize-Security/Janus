from flask import Blueprint, render_template, redirect, url_for, flash
from flask import request as flask_request
from flask_login.utils import login_user
from werkzeug.wrappers import request
from app.forms.auth import RegisterForm, LoginForm
from app.models.system_user import SystemUser as User
from app.models.reg_key import RegKey 
from app import db
from app.config import FormsConfig


auth = Blueprint('auth', __name__)


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(flask_request.form)
    res = form.validate_on_submit()
    if res:
        username = form.username.data
        email = form.email.data
        password = form.password_1.data
        reg_key = form.reg_key.data
        is_active = 1

        try:
            valid_key = RegKey.query.filter_by(reg_key).first()
            if valid_key.email != email or valid_key is None:
                flash('Invalid key')
                redirect(url_for('registration'))
        except Exception as e:
            print(str(e))

        try:
            if User.query.filter_by(email=email):
                flash('User already registered')
                return redirect(url_for("login"))
            else:
                user = User(username, email, password, reg_key, is_active)
                db.session.add(user)
                db.session.commit()
                flash('Registered successfully')
                return redirect(url_for('login'))
        except Exception as e:
            print(str(e))
    
    if form.errors:
        flash(FormsConfig.SUBMIT_ERROR)

    return render_template("register.html", form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user.check_password(form.password.data) and user is not None:
                login_user(user)
                next = request.args.get('next')
                if next == None or not next[0] == '/':
                    next = url_for('home')
                return redirect(next)
        except Exception as e:
            print(str(e))

    return render_template("login.html", form=form)
