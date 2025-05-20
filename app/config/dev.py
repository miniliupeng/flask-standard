import os
from .base import BaseConfig, basedir


class Development(BaseConfig):
    PORT = 6000
    DEBUG = True
    ENV = "dev"
    TESTING = True
    SQLALCHEMY_ECHO = True  # 打印SQL