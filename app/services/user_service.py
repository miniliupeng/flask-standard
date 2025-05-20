from app import db
from app.models import User

class UserService:
    """用户服务类，处理用户相关业务逻辑"""
    
    @staticmethod
    def get_all_users():
        """获取所有用户"""
        return User.query.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        """根据ID获取用户"""
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_email(email):
        """根据邮箱获取用户"""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def create_user(username, email, password):
        """创建新用户"""
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update_user(user, **kwargs):
        """更新用户信息"""
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user):
        """删除用户"""
        db.session.delete(user)
        db.session.commit()
    
    @staticmethod
    def authenticate(email, password):
        """验证用户凭证"""
        user = UserService.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None 