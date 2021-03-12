"""FlaskのConfigを提供する"""
import os
from sqlalchemy import create_engine

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/mydb?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'Rikizou105'),
        'host': os.getenv('DB_HOST', 'localhost'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig

# #DB接続用のインスタンスを作成
# ENGINE = create_engine(
#     Config,
#     convert_unicode=True,
#     echo=True  #SQLをログに吐き出すフラグ
# )

# #上記のインスタンスを使って、MySQLとのセッションを張ります
# session = scoped_session(
#     sessionmaker(
#         autoflush = False,
#         autocommit = False,
#         bind = ENGINE,
#     )
# )
