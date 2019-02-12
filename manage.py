# 导入flask_migrate扩展和script扩展
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import create_app, db

# 使用工厂函数创建，并传入配置模式
app = create_app('development')

# 添加拓展命令行
manage = Manager(app)

# 数据库迁移
Migrate(app, db)
# 添加迁移命令
manage.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manage.run()
