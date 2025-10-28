import click
from .services.alert_service import process_alerts
from app import create_app


@click.command('initTasks')
def task_maestro():
    try:
        click.echo('Rotina de busca iniciada...')
        
        app = create_app()
        with app.app_context():
            process_alerts()

        click.echo(click.style('Rotina finalizada com sucesso!', fg='green'))

    except Exception as e:
        click.echo(click.style("ERRO: Rotina interrompida. >> Verifique o e-mail de erro para detalhes.", fg='red'))