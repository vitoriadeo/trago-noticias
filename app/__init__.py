from flask import Flask

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app.controllers import home_controller
    app.register_blueprint(home_controller.bp)

    return app