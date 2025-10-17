# Configuração, registros e manipulação de erros
# Define como minha aplicação Flask é criada e configurada.

import os 
from flask import Flask, render_template
from .config import ProdConfig, DevConfig, Config
from app.controllers import home_controller
from . import database_manager

def create_app():
    app = Flask(__name__)
    

    # CONDICIONAL PARA VARIÁVEL DE AMBIENTE
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)


    # BANCO DE DADOS
    database_manager.init_app(app)


    # BLUEPRINT - Registro
    app.register_blueprint(home_controller.bp)
    app.register_blueprint(home_controller.bp_about)

    # FLASK-CLI - Registra comandos feitos no tasks.py
    from app import tasks
    app.cli.add_command(tasks.task_maestro)


    # MANIPULAÇÕES DE ERROS
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):

        return render_template('errors/500.html'), 500
    return app