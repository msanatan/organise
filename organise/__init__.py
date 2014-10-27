from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from organise.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

from organise.views import todos
app.register_blueprint(todos, url_prefix='/todos')
