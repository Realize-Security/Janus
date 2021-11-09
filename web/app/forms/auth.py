from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, Regexp, EqualTo, ValidationError
from app.config import SecurityConfig
from app.models.system_user import SystemUser as User
from app.config import SecurityConfig


class RegisterForm(FlaskForm):

    REG_ERROR = SecurityConfig.REGISTRATION_ERROR

    required_message = "This field is required"
    username = StringField("Username", validators=[DataRequired(message=required_message)])
    email = StringField("Email", validators=[Email()])
    password_1 = PasswordField("Password", validators=[Length(min=SecurityConfig.PASSWORD_MIN_LENGTH)])
    password_2 = PasswordField("Confirm password", validators=[EqualTo(fieldname=password_1, message='Passwords must match')])
    reg_key = StringField("Registration Token", validators=[Regexp(regex=SecurityConfig.REG_TOKEN_REGEX)])
    submit = SubmitField("Register")


    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(self.REG_ERROR)


    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(self.REG_ERROR)


class LoginForm(FlaskForm):
    
    required_message = "This field is required"
    username = StringField("Username", validators=[DataRequired(message=required_message)])
    email = StringField("Email", validators=[Email(), DataRequired(message=required_message)])
    password = PasswordField("Password", validators=[DataRequired(message=required_message)])
    submit = SubmitField("Register")
