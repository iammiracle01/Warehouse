import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger



db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///warehouse.db"
    db.init_app(app)

    swagger = Swagger(
        app,
        template={
            "info": {
                "title": "My Flask API",
                "description": "An example API using Flask and Swagger",
                "version": "1.0.0",
            }
        },
    )

    with app.app_context():
        from . import models
        from .controllers import main

        app.register_blueprint(main)

        if not os.path.exists('warehouse.db'):
            db.create_all()

    return app
