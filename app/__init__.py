from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/metricsdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from app import models

def create_app():
    from app.views import metrics_api
    app.register_blueprint(metrics_api)
    return app

