from .error import error
from .zhihu import zhihu
from .wechat import wechat


def init_view(app):
    app.register_blueprint(zhihu)
    app.register_blueprint(error)
    app.register_blueprint(wechat)

