from flask import Blueprint, render_template, send_from_directory


core = Blueprint('core', __name__)


@core.get('/')
def index():
    return render_template("index.html")


@core.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(core.config["STATIC_FOLDER"], filename)


# @core.route("/static/images/<path:filename>")
# def imagefiles(filename):
#     return send_from_directory(core.config["STATIC_FOLDER"] + "/", filename)

