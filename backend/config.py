import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://user:password@db:3306/spellwiki"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
