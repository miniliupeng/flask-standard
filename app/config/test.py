import os
from .base import BaseConfig, basedir


class Test(BaseConfig):
    PORT = 5000
    DEBUG = True
    ENV = "test"
    TESTING = True
