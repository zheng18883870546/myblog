"""__author郑晓卫"""
import redis

from flask import Flask
from flask_script import Manager
from flask_session import Session

from back.models import db
from back.views import back_blue
from web.views import web_blue

app = Flask(__name__)
app.register_blueprint(blueprint=back_blue, url_prefix='/back')
app.register_blueprint(blueprint=web_blue, url_prefix='/web')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zheng123456@47.102.99.211:3306/myblog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='47.102.99.211', port=6379, password='zheng123456')

Session(app)
app.secret_key = '123456789dsadsad'
manage = Manager(app)

if __name__ == '__main__':
    manage.run()