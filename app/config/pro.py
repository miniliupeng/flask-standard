from .base import BaseConfig


class Production(BaseConfig):
    PORT = 5000
    DEBUG = False
    ENV = "prod"
    TESTING = False
