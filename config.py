import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_PATH = os.path.join(basedir, 'biblios.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
