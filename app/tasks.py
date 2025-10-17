import click
from .services.alert_service import process_alerts


@click.command('initTasks')
def task_maestro(): #Busca, execução, filtro e envio
    click.echo('Rotina de busca iniciada...')

    process_alerts()

    click.echo('Rotina finalizada!')
