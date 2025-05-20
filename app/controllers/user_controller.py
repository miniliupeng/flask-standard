from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app import db

# 创建用户蓝图
user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/profile')
def profile():
    """显示用户个人资料"""
    # 获取当前用户
    user = AuthService.get_current_user()
    if not user:
        flash('请先登录', 'error')
        return redirect(url_for('auth.login'))
    
    return render_template('user/profile.html', user=user)

@user_bp.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    """编辑用户个人资料"""
    # 获取当前用户
    user = AuthService.get_current_user()
    if not user:
        flash('请先登录', 'error')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # 获取表单数据
        username = request.form.get('username')
        
        # 验证数据
        if not username:
            flash('用户名不能为空', 'error')
            return render_template('user/edit_profile.html', user=user)
        
        # 更新用户信息
        try:
            UserService.update_user(user, username=username)
            flash('个人资料已更新', 'success')
            return redirect(url_for('user.profile'))
        except Exception as e:
            flash(f'更新失败: {str(e)}', 'error')
            return render_template('user/edit_profile.html', user=user)
    
    # GET请求，显示编辑表单
    return render_template('user/edit_profile.html', user=user)

@user_bp.route('/change_password', methods=['GET', 'POST'])
def change_password():
    """修改密码"""
    # 获取当前用户
    user = AuthService.get_current_user()
    if not user:
        flash('请先登录', 'error')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # 获取表单数据
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        # 验证数据
        if not current_password or not new_password or not confirm_password:
            flash('所有字段都必须填写', 'error')
            return render_template('user/change_password.html')
        
        if new_password != confirm_password:
            flash('新密码两次输入不一致', 'error')
            return render_template('user/change_password.html')
        
        if not user.check_password(current_password):
            flash('当前密码不正确', 'error')
            return render_template('user/change_password.html')
        
        # 更新密码
        try:
            user.set_password(new_password)
            db.session.commit()
            flash('密码已更新', 'success')
            return redirect(url_for('user.profile'))
        except Exception as e:
            flash(f'更新失败: {str(e)}', 'error')
            return render_template('user/change_password.html')
    
    # GET请求，显示修改密码表单
    return render_template('user/change_password.html') 