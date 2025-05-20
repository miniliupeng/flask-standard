from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):  # 用户数据模型
    __tablename__ = "users"  # 数据库表名

    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(64), unique=True, index=True)  # 用户名
    email = db.Column(db.String(120), unique=True, index=True)  # 邮箱
    password_hash = db.Column(db.String(128))  # 密码哈希

    def __init__(self, username, email, password):  # 构造函数
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):  # 设置密码
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):  # 验证密码  通常会在登录视图中使用
        return check_password_hash(self.password_hash, password)

    def __repr__(self):  # 字符串表示   在调试和日志记录时会自动使用
        return f"<User {self.username}>"
