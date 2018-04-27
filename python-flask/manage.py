import os
from flask import url_for
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model import db
from initialize import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    "Just say hello"
    print ("hello")


@manager.command
def list_routes():
    "List API endpoints"
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    manager.run()


    