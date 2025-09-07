import os 
from flask import Flask, render_template
from .config import ProdConfig, DevConfig

def create_app():
    app = Flask(__name__)
    
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)

    from app.controllers import home_controller
    app.register_blueprint(home_controller.bp)

    # MANIPULAÇÕES DE ERROS
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):

        # para reverter sessão em caso de erros >> db.session.rollback()
        return render_template('errors/500.html'), 500


    return app