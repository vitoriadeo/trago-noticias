import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def coleta(termo):
    dicionario_de_noticias = {}
    resultados_noticias = []
    base_url = "https://news.google.com"

    print(f"Iniciando buscas por {termo}...")

    try:
        resposta = requests.get(f'https://news.google.com/search?q={termo}&hl=pt-BR&gl=BR&ceid=BR%3Apt-419')
        resposta.raise_for_status()

        sopa = BeautifulSoup(resposta.text, "html.parser")
        amontoado_html = sopa.find_all("article", limit=5) #div class m5k28 em funcionamento data 14/09/2025

        for noticia in amontoado_html:
            tag_a = noticia.find('a')
            tag_data = noticia.find('time')
            data_publicacao = tag_data.get('datetime') if tag_data else None


            if tag_a:
                link_relativo = tag_a['href']
            else:
                print('SEM LINK. PULANDO!!')
                continue

            link_completo = urljoin(base_url, link_relativo)

            tituloBruto = noticia.get_text()
            fonte_titulo = tituloBruto.split('Mais', 1)
            titulo = fonte_titulo[1]
            fonte = fonte_titulo[0]

            dicionario_de_noticias['Fonte'] = fonte
            dicionario_de_noticias['Data'] = data_publicacao
            dicionario_de_noticias['Titulo'] = titulo
            dicionario_de_noticias['Link completo'] = link_completo

            resultados_noticias.append(dicionario_de_noticias.copy())

        return resultados_noticias
    except requests.exceptions.RequestException as e:
        print(f"LOG - Erro de conexão: {e}")
        return None