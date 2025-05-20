from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app.services.auth_service import AuthService

# 创建认证蓝图
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    """用户注册"""
    if request.method == "POST":
        # 从表单获取数据
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # 使用AuthService处理注册
        success, result = AuthService.register(username, email, password)

        if success:
            flash("注册成功，请登录", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(result, "error")
            return render_template("auth/register.html")


@auth_bp.route("/login", methods=["POST"])
def login():
    """用户登录"""
    if request.method == "POST":
        # 从表单获取数据
        email = request.form.get("email")
        password = request.form.get("password")

        # 使用AuthService处理登录
        success, result = AuthService.login(email, password)

        if success:
            flash("登录成功", "success")
            return redirect(url_for("main.index"))
        else:
            flash(result, "error")
            return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    """用户登出"""
    AuthService.logout()
    flash("已登出", "success")
    return redirect(url_for("main.index"))
