"""FlaskのConfigを提供する"""
import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'rikizou'),           # localの情報に合わせて変更すること
        'password': os.getenv('DB_PASSWORD', '{Rikizou105d}'),       # localの情報に合わせて変更すること
        'host': os.getenv('DB_HOST', 'localhost'),      # localの情報に合わせて変更すること
        'db_name': os.getenv('DB_DATABASE', 'mydb'),    # localの情報に合わせて変更すること
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
