from flask import Flask
from .config import ProdConfig

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProdConfig)

    from app.controllers import home_controller
    app.register_blueprint(home_controller.bp)

    return app