from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_delete = db.Column(db.Boolean(), default=0)
    create_time = db.Column(db.DateTime, default=datetime.now())
    # user_info = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    __tablename__='user'

    def save(self):
        db.session.add(self)
        db.session.commit()


class ArticleType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_name = db.Column(db.String(10), unique=True, nullable=False)
    arts = db.relationship('Article', backref='tp')

    __tablename__ = 'art_type'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    type = db.Column(db.Integer, db.ForeignKey('art_type.id'))


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(30), unique=True, nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(30), nullable=False)
    is_logout = db.Column(db.Boolean, nullable=False)
    # u_id = db.relationship('User', backref='ui')
