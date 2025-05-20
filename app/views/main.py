from flask import render_template
from app.views import main_bp


@main_bp.route("/")
def index():
    return render_template("index.html", title="首页")


@main_bp.route("/about")
def about():
    return render_template("about.html", title="关于")
