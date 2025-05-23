from .base import BaseConfig


class Development(BaseConfig):
    PORT = 6000
    DEBUG = True
    ENV = "dev"
    TESTING = True
    SQLALCHEMY_ECHO = True  # 打印SQL
