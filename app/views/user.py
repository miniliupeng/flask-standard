from flask import render_template, redirect, url_for, flash
from app.views import main_bp
from app.services.auth_service import AuthService


@main_bp.route("/profile")
def profile():
    """显示用户个人资料"""
    # 获取当前用户
    user = AuthService.get_current_user()
    if not user:
        flash("请先登录", "error")
        return redirect(url_for("auth.login"))

    return render_template("user/profile.html", user=user)


@main_bp.route("/edit", methods=["GET", "POST"])
def edit_profile():
    """编辑用户个人资料"""
    # 获取当前用户
    user = AuthService.get_current_user()
    if not user:
        flash("请先登录", "error")
        return redirect(url_for("auth.login"))
    # GET请求，显示编辑表单
    return render_template("user/edit_profile.html", user=user)


@main_bp.route("/change_password")
def change_password():
    # GET请求，显示修改密码表单
    return render_template("user/change_password.html")
