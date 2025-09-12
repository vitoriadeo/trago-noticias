import click

# TESTANDO CLI
@click.command('TesteCLI')
def TesteCLI():
    click.echo('Testando ferramenta CLI...')

# CÓDIGO EM DESENVOLVIMENTO
@click.command('initTasks')
def task_maestro(): #Busca, execução, filtro e envio
    click.echo('Rotina de busca iniciada...')

    # FUNÇÕES AUXILIARES
    # alertas_do_dia(): Essa função terá a lógica de descobrir qual é o dia da semana e consultar o banco de dados para retornar os alertas corretos.
    # executar_webScrapping(): Para buscas de termos
    # filtragem(noticias_brutas): Com allowlist. Comparação com noticias brutas.
    # envioNoticias(alerta, noticiasfiltradas): 

    click.echo('Rotina finalizada!')
