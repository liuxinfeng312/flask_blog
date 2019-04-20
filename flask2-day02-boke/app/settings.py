from datetime import timedelta


class BaseConfig(object):
    SECRET_KEY = 'JKHJH4654532163@%#^&^%&%$^@^'
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False





class DevelopConfig(BaseConfig):
        DEBUG=True
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1204@127.0.0.1:3306/flask2_boke'
        MAIL_SERVER='smtp.163.com'
        MAIL_USERNAME='liuxinfeng312@163.com'
        MAIL_PASSWORD='441621asd'


config={

    'develop':DevelopConfig,
    'default':DevelopConfig,


}


def init_setting(app,env_name):


    app.config.from_object(config.get(env_name))
