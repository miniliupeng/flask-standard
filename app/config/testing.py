import os
from .default import Config, basedir


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test-app.db")
    WTF_CSRF_ENABLED = False
