from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)

app.config.from_object('app.config.DevelopmentConfig')

from app.main.views import main_blueprint

app.register_blueprint(main_blueprint)