import os

APP_TITLE = "Janus"
VICTIM_TITLE = ""


class AppConfig(object):
    """Parent configuration class."""
    basedir = os.path.abspath(os.path.dirname(__file__))
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    LOG_ENABLED = os.getenv('LOG_ENABLED')



class SecurityConfig(object):
    """Security specific strings and configs"""
    PASSWORD_MIN_LENGTH = 10
    REG_TOKEN_REGEX = r"[a-z0-9]{64,64}"
    USER_IS_ACTIVE = "is_active"
    REGISTRATION_ERROR = 'Please check your details and try again'


class FormsConfig(object):
    """User forms field strings"""
    USERNAME = "username"
    EMAIl = "email"
    PASS_1 = "password_1"
    PASS_2 = "password_2"
    REG_KEY = "reg_key"
    PASS_SUBMIT = "password"


class LogConf(object):
    """Logging config strings"""
    LOGPATH = "/vol/log"
    LOGFILE = "flask.log"
    DEBUG = "debug"
    INFO = "info"
    WARN = "warning"
    ERROR = "error"
    CRIT = "critical"