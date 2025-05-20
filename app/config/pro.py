import os
from .base import BaseConfig, basedir


class Production(BaseConfig):
    PORT = 5000
    DEBUG = False
    ENV = "prod"
    TESTING = False
