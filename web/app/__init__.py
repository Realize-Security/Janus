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

# if AppConfig.DEBUG:
#     import debugpy
#     debugpy.listen(("0.0.0.0", 5678))


db = SQLAlchemy(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app.routes.core import core
from app.routes.auth import auth


# @app.after_request
# def after_request(response):
#     timestamp = strftime('[%Y-%b-%d %H:%M]')
#     logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#     return response


# @app.errorhandler(Exception)
# def exceptions(e):
#     tb = traceback.format_exc()
#     timestamp = strftime('[%Y-%b-%d %H:%M]')
#     logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
#     return "True"


app.register_blueprint(core)
app.register_blueprint(auth)
