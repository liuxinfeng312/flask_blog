from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db=SQLAlchemy()
migrate=Migrate()
cache=Cache(config={'CACHE_TYPE':'redis'})
mail=Mail()


def init_exts(app):
    db.init_app(app)
    migrate.init_app(app,db)
    cache.init_app(app)
    mail.init_app(app)