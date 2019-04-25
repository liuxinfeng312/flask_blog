from datetime import datetime

from app.exts import db


class User(db.Model):#用户表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256),nullable=False)
#     定义wai建
    article_id=db.Column(db.Integer, db.ForeignKey('article.id'),nullable=True)



class Photo(db.Model):#照片表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url=db.Column(db.String(100),unique=True)
    title=db.Column(db.String(100))
    context=db.Column(db.String(255))


class Article(db.Model):#文章表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time=db.Column(db.DateTime, default=datetime.now)
    title=db.Column(db.String(100))
    context=db.Column(db.Text)
    user=db.relationship('User',backref='user')


class Backuser(db.Model):#后台用户表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))
