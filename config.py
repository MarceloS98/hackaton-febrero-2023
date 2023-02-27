class Config():
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
$env:FLASK_APP = "src"
$env:FLASK_DEBUG = 1
'''