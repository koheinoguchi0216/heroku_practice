"""FlaskのConfigを提供する"""
import os

# Flask
DEBUG = False

# local_config.pyファイルを読み込み
try:
    from .local_config import *
except ImportError:
    pass




class DevelopmentConfig:

    if not DEBUG:
        # SECRET_KEY設定
        SECRET_KEY = os.environ['SECRET_KEY']

        # Flask
        DEBUG = True

        # SQLAlchemy
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
            'user': os.getenv('DB_USER', os.environ['DB_USERNAME']),           # localの情報に合わせて変更すること
            'password': os.getenv('DB_PASSWORD', os.environ['DB_PASSWORD']),       # localの情報に合わせて変更すること
            'host': os.getenv('DB_HOST', os.environ['DB_HOSTNAME']),      # localの情報に合わせて変更すること
            'db_name': os.getenv('DB_DATABASE', os.environ['DB_NAME']),    # localの情報に合わせて変更すること
        })
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
