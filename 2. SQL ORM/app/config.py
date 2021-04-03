import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'racks.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SERVER_NAME = '127.0.0.1:5006'