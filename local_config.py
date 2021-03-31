import os

DEBUG = True

SECRET_KEY = 'SECRET_KEY'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/mydb?charset=utf8'.format(**{
    'user': os.getenv('DB_USER', 'rikizou'),
    'password': os.getenv('DB_PASSWORD', '{Rikizou105d}'),
    'host': os.getenv('DB_HOST', 'localhost'),
})
