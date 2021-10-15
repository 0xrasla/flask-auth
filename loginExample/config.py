from loginExample import models


class Config(object):
    SECRET_KEY = "ahkaifya8f8a7fa8f"
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
