from flask import render_template
from app.views import main_bp


@main_bp.route("/register")
def register():
    return render_template("auth/register.html")


@main_bp.route("/login")
def login():
    return render_template("auth/login.html")
