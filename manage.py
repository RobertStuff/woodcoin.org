from flask.ext.script import Manager, Server

from app import app

app.config.from_object('app.config.DevelopmentConfig')

manager = Manager(app)

manager.add_command ("runserver", Server (host='0.0.0.0')) 

if __name__ == '__main__':
	manager.run()