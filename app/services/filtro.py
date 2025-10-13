from pathlib import Path

def carrega_sites_noticias():
    caminho_atual = Path(__file__).resolve()
    caminho_arquivo = caminho_atual.parent.parent
    caminho_arquivo = caminho_arquivo / 'allowlist.txt'

    caminho_arquivo = Path('app/allowlist.txt')

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dominios = [sites.split(', ') for sites in arquivo]

    dominios = set(dominios[0])

    return dominios


def filtragem(resultado):
    dominios = carrega_sites_noticias()

    noticias_filtradas = []

    for noticia in resultado:
        for fonteChave, siteValor in noticia.items():
            if siteValor in dominios:
                noticias_filtradas.append(noticia)

    return noticias_filtradas
