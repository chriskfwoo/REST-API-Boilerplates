import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model import db
from run import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    "Just say hello"
    print ("hello")


if __name__ == '__main__':
    manager.run()


    