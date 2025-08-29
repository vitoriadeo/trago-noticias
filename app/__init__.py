import os 
from flask import Flask
from .config import ProdConfig, DevConfig

def create_app():
    app = Flask(__name__)
    
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)

    from app.controllers import home_controller
    app.register_blueprint(home_controller.bp)

    return app