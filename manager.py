from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
import os

# env获取环境变量FLASK_ENV，若没有环境变量，默认为“develop”
env = os.environ.get("FLASK_ENV", "develop")

app = create_app(env)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

