import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'sample.db'
#USERNAME = 'admin'
#PASSWORD = 'admin'
CSRF_ENABLED = True
#WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the fullpath for database
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = True


