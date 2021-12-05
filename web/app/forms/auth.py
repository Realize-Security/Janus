from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, Regexp, EqualTo, ValidationError, Optional
from app.config import SecurityConfig
from app.models.system_user import SystemUser as User
from app.config import SecurityConfig


class RegisterForm(FlaskForm):

    REG_ERROR = SecurityConfig.REGISTRATION_ERROR
    PASSWORD_MIN = SecurityConfig.PASSWORD_MIN_LENGTH
    required_message = "This field is required"
    min_length_message = f"Password Requirements: Must be {PASSWORD_MIN} characters in length and contain at least: 1 upper case letter, one lower case letter, a number and a special character."

    username = StringField("Username", validators=[DataRequired(message=required_message)])
    email = StringField("Email", validators=[Email(), DataRequired(message=required_message)])
    password_1 = PasswordField("Password", validators=[
        Length(min=PASSWORD_MIN),
        Regexp(regex=SecurityConfig.PASSWORD_COMPLEXITY),
        DataRequired(message=min_length_message)
        ]
    )
    password_2 = PasswordField("Confirm Password", validators=[EqualTo(fieldname='password_1', message='Passwords must match')])
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
