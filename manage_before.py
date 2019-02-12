from flask import Flask
# 连接数据库的包
from flask_sqlalchemy import SQLAlchemy
# 导入redis模包
import redis
# 使用flask_session扩展包
from flask_session import Session
# 命令行启动包
from flask_script import Manager
# 数据库迁移包
from flask_migrate import Migrate, MigrateCommand
# 防止csrf攻击包
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world!"


class Config(object):
    """工程配置信息"""

    # 开启debug模式
    DEBUG = True
    # 基本数据库的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/info21'
    # 动态追踪修改设置，如为设置会提示警告？？？
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    # 状态保持的基本配置
    SECRET_KEY = 'stPkMpYjBvYF26UsrwxR898oyasgdbX853nOjShiIBZoCHzYKI76cpaRUzdU'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # ？？？
    SESSION_USE_SIGNER = True
    # session存活周期
    PERMANENT_SESSION_LIFETIME = 86400


app.config.from_object(Config)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
db = SQLAlchemy(app)
Session(app)
CSRFProtect(app)
# 实例化管理对象
manage = Manager(app)
# 数据库迁移
Migrate(app, db)
# 添加迁移命令
manage.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manage.run()
