from .base import BaseConfig


class Test(BaseConfig):
    PORT = 5000
    DEBUG = True
    ENV = "test"
    TESTING = True
