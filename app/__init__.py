from flask import Flask
from app.settings import envs
from app.extensions import init_ext
from app.views import init_view


def create_app(env):
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(envs.get(env))
    # 初始化l路由
    init_view(app=app)
    # 初始化第三方扩展库
    init_ext(app=app)
    return app
