import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(nome, email, termo, noticias):
    remetente = os.environ.get('MAIL_DEFAULT_SENDER')
    remetente_nome = "Trago Notícias"
    destinatario = email
    api_key = os.environ.get('SENDGRID_API_KEY')

    lista_noticias = []
    for noticia in noticias:
        titulo = noticia.get('Titulo', 'Sem titulo')
        link = noticia.get('Link completo', '#')
        fonte = noticia.get('Fonte', 'Fonte desconhecida')
        item_html = f"<li><a href='{link}' target='_blank'>{titulo}</a> ({fonte})</li>"
        lista_noticias.append(item_html)

        html_da_lista = "".join(lista_noticias)

    html_content = f"""
        <h3>📰 Alerta de notícias: {termo} | Trago Notícias</h3>
        <hr>
        <p>Oiê, {nome}!</p>
        <p>Trago boas notícias! Nossa busca encontrou as seguintes novidades sobre o seu alerta para o termo '{termo}':</p>
        <ul>
            {html_da_lista}
        </ul>
        <p>Esperamos que as informações sejam úteis!</p>
        <p>Atenciosamente,<br>Equipe Trago Notícias</p>
        <hr>
        <small>Você está recebendo esse email porque se cadastrou para receber um alerta sobre {termo} no site <a href="https://tragonoticias.site/" target="_blank">Trago Noticias</a>. Caso queira cancelar, basta responder esse email informando que deseja a retirada dos seus dados do nosso banco de dados.</small>
    """

    message = Mail(
        from_email=f"{remetente_nome} <{remetente}>",
        to_emails=destinatario,
        subject=f"Trago Notícias: Novidades sobre '{termo}'",
        html_content=html_content
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f">> Email sobre o alerta {termo} enviado para [{nome} - {destinatario}] | status code: {response.status_code}")
        return True, print("Email enviado com sucesso!")
    
    except Exception as e:
        print(f"LOG EMAIL: {e}")
        return False, print(f"Ocorreu um erro ao enviar o email: {e}")