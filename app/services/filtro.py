from web_scraper import coleta

resultado = coleta(termo)

caminho_arquivo = r'C:/Users/Vitória/Documents/projetos/trago-noticias/app/'
caminho_arquivo += 'allowlist.txt'

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dominios = [sites.split(', ') for sites in arquivo]

dominios = set(dominios[0])

#fonte = resultado[0]['Fonte']

noticias_filtradas = []

for noticia in resultado:
    for fonteChave, siteValor in noticia.items():
        if siteValor in dominios:
            noticias_filtradas.append(noticia)

print(noticias_filtradas)
