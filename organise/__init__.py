from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from organise.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

from organise.views.todos import todos
from organise.views.main import main
app.register_blueprint(todos, url_prefix='/todos')
app.register_blueprint(main)