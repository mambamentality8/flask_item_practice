from logging.handlers import RotatingFileHandler

from config import Config, config
from flask import Flask
# 配置日志包
import logging
from flask_sqlalchemy import SQLAlchemy
# 导入redis模块
import redis
# 使用flask_session扩展包
from flask_session import Session
# 导入CSRF包
from flask_wtf.csrf import CSRFProtect


def setup_log(config_name):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)
    # 配置项目日志
    setup_log(config_name)
    # 配置
    app.config.from_object(Config[config_name])
    # 配置数据库
    db = SQLAlchemy(app)
    # 配置redis
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 开启CSRF保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    return app
