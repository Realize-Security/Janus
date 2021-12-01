from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import traceback
import logging
from app.config import LogConf, AppConfig
from time import strftime
import os


app = Flask(__name__, static_url_path='/static')
app.config.from_object("app.config.AppConfig")


logger = logging.getLogger('werkzeug')
logpath = os.path.join(LogConf.LOGPATH, LogConf.LOGFILE )
handler = logging.FileHandler(logpath)
logger.addHandler(handler)


db = SQLAlchemy(app)
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

if AppConfig.DEBUG:
    from flask_debugtoolbar import DebugToolbarExtension
    app.debug = True
    toolbar = DebugToolbarExtension(app)

from app.routes.core import core
from app.routes.auth import auth


if AppConfig.LOG_ENABLED:
    @app.after_request
    def after_request(response):
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
        return response


    @app.errorhandler(Exception)
    def exceptions(e):
        tb = traceback.format_exc()
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
        return "Error was logged"


app.register_blueprint(core)
app.register_blueprint(auth)

