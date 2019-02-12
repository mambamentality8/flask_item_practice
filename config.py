import redis
import logging


class Config(object):
    """工程配置信息"""
    SECRET_KEY = 'stPkMpYjBvYF26UsrwxR898oyasgdbX853nOjShiIBZoCHzYKI76cpaRUzdU'

    # 基本数据库的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/info21'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    # session 配置
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    pass


# 定义配置字典
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

# 添加日志等级
LOG_LEVEL = logging.INFO


class ProductionConfig(Config):
    LOG_LEVEL = logging.ERROR
