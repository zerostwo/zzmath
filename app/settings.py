import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbInfo):
    engine = dbInfo.get("ENGINE") or "sqlite"
    driver = dbInfo.get("DRIVER") or "sqlite"
    user = dbInfo.get("USER") or ""
    password = dbInfo.get("PASSWORD") or ""
    host = dbInfo.get("HOST") or ""
    port = dbInfo.get("PORT") or ""
    name = dbInfo.get("NAME") or ""

    return "{engine}+{driver}://{user}:{password}@{host}:{port}/{name}".format(engine=engine, driver=driver, user=user,
                                                                               password=password, host=host,
                                                                               port=port, name=name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "duansq"


# 开发环境
class DevelopConfig(Config):
    DEBUG = True
    dbInfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "duansq",
        "PASSWORD": "981211",
        "HOST": "47.112.25.206",
        "PORT": "3306",
        "NAME": "zzmath"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbInfo)


# 测试环境
class TestConfig(Config):
    TESTING = True
    dbInfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "981211",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "zzmath"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbInfo)


# 演示环境
class StagingConfig(Config):
    dbInfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "981211",
        "NAME": "zzmath",
        "HOST": "localhost",
        "PORT": "3306"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbInfo)


# 生产环境
class ProductConfig(Config):
    dbInfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "981211",
        "NAME": "zzmath",
        "HOST": "localhost",
        "PORT": "3306"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbInfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
