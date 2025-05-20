# __init__.py文件的作用
# 它告诉Python这个目录是一个包
# 它在导入包时自动执行

# 模型包

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 创建数据库实例

from .user import User  # 导入User模型
