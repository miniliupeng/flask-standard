import os
from urllib import parse

class BaseConfig:
    """
    基础配置
    """

    APP_AUTHOR = "liupeng"  # 作者
    WHITE_LIST = []  # 权限白名单
    DB_HOST = os.getenv("DB_HOST", "localhost")  # 数据库ip
    DB_PORT = os.getenv("DB_PORT", "3306")  # 数据库端口
    DB_NAME = os.getenv("DB_NAME", "flaskapp")  # 数据库名称
    DB_USER = os.getenv("DB_USER", "root")  # 数据库用户
    DB_PASSWORD = os.getenv("DB_PASSWORD", "123456")  # 数据库密码
    # 数据库相关配置开始
    # 防止密码中有特殊字符，需要使用parse.quote_plus进行转义
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{parse.quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 5,
        'pool_timeout': 90,
        'pool_recycle': 7200,
        'max_overflow': 1024
    }
    # 数据库相关配置结束
    JSON_AS_ASCII = False  # 禁止中文转义'

    # ------redis相关配置------
    # 环境变量中获取数据库REDIS_HOST
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    # 环境变量中获取数据库REDIS_PORT
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    # 环境变量中获取数据库REDIS_PASSWORD
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
    # REDIS_URL = "redis://:password@localhost:6379/0" --->flask-redis需要该配置
    REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
    # ------redis相关配置------

    # ------token相关配置------
    # token 过期时间- 单位是s  # 2小时
    TOKEN_EXPIRE_TIMEOUT = int(os.getenv("TOKEN_EXPIRE_TIMEOUT", 60 * 60 * 2))
    # token-key
    TOKEN_KEY = os.getenv("TOKEN_KEY", "token")
    # token 前辍
    TOKEN_KEY_PREFIX = os.getenv("TOKEN_KEY", "flaskapp:")
    # 超级管理员id
    SUPER_ADMIN_ID = os.getenv("SUPER_ADMIN_ID", 1)
    # Token存储策略
    TOKEN_STRATEGY = os.getenv("TOKEN_STRATEGY", "cache")
    # ------token相关配置------

    

    @staticmethod
    def init_app(app):
        pass
