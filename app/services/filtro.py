from web_scraper import coleta
from pathlib import Path

resultado = coleta(termo)

caminho_atual = Path(__file__).resolve()
caminho_arquivo = caminho_atual.parent.parent
caminho_arquivo = caminho_arquivo / 'allowlist.txt'

caminho_arquivo = Path('app/allowlist.txt')

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dominios = [sites.split(', ') for sites in arquivo]

dominios = set(dominios[0])

noticias_filtradas = []

for noticia in resultado:
    for fonteChave, siteValor in noticia.items():
        if siteValor in dominios:
            noticias_filtradas.append(noticia)

print(noticias_filtradas)
