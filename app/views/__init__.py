from .error import error
from .zhihu import zhihu


def init_view(app):
    app.register_blueprint(zhihu)
    app.register_blueprint(error)
