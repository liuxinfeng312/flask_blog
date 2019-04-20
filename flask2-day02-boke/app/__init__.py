from app.exts import init_exts
from app.settings import init_setting
from app.views import init_views


def create_app(env_name='default'):
    from flask import Flask

    app = Flask(__name__)


    init_setting(app,env_name)

    init_exts(app)

    init_views(app)


    return app