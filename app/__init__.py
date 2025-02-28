from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import routes_app

app = Flask(__name__)

CORS(app)

app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(routes_app)

with app.app_context():
    db.create_all()