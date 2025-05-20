from flask import session
from app.services.user_service import UserService

class AuthService:
    """认证服务类，处理身份验证相关业务逻辑"""
    
    @staticmethod
    def login(email, password):
        """用户登录
        
        Args:
            email (str): 用户邮箱
            password (str): 用户密码
            
        Returns:
            tuple: (成功状态, 用户对象或错误消息)
        """
        # 参数验证
        if not email or not password:
            return False, "邮箱和密码不能为空"
        
        # 验证用户凭证
        user = UserService.authenticate(email, password)
        if not user:
            return False, "邮箱或密码不正确"
        
        # 登录成功，设置会话
        session['user_id'] = user.id
        return True, user
    
    @staticmethod
    def register(username, email, password):
        """用户注册
        
        Args:
            username (str): 用户名
            email (str): 邮箱
            password (str): 密码
            
        Returns:
            tuple: (成功状态, 用户对象或错误消息)
        """
        # 参数验证
        if not username or not email or not password:
            return False, "所有字段都必须填写"
        
        # 检查用户是否已存在
        if UserService.get_user_by_email(email):
            return False, "该邮箱已被注册"
        
        # 创建新用户
        try:
            user = UserService.create_user(username, email, password)
            return True, user
        except Exception as e:
            return False, f"注册失败: {str(e)}"
    
    @staticmethod
    def logout():
        """用户登出"""
        session.pop('user_id', None)
        return True
    
    @staticmethod
    def get_current_user():
        """获取当前登录用户
        
        Returns:
            User: 当前登录用户对象，如未登录则返回None
        """
        user_id = session.get('user_id')
        if user_id:
            return UserService.get_user_by_id(user_id)
        return None
    
    @staticmethod
    def is_authenticated():
        """检查用户是否已认证
        
        Returns:
            bool: 是否已认证
        """
        return AuthService.get_current_user() is not None 