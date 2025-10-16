from app.database_manager import get_db
from .web_scraper import coleta
from .filtro import carrega_sites_noticias, filtragem
from .sender_email import send_email
from datetime import timedelta, timezone, datetime
import datetime

# FUNÇÃO PRINCIPAL.
# O EMAIL ADD AO FORMULÁRIO JÁ EXISTE?
def handle_alert_submission(nome, email, termo, frequencia):
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute("select id_usuario from usuario where email = %s", (email,))
        resultado = cursor.fetchone()

        if resultado:
            user_id = resultado[0]
            print(f"Usuário existente. ID {user_id}")
            add_alert_to_existing_user(user_id, termo, frequencia, cursor)

        else:
            print("Novo usuário! Criando cadastro e alerta...")
            add_user_and_alert(nome, email, termo, frequencia, cursor)

        db.commit()
        print("Operação concluída e salva do banco de dados.")

    except Exception as e:
        db.rollback()
        print(f"Ocorreu um erro. A transação foi desfeita: {e}")
        raise e
    finally:
        cursor.close()


# FUNÇÃO AUXILIAR
# SE EXISTIR
def add_alert_to_existing_user(user_id, termo, frequencia, cursor):

    cursor.execute(
        "insert into alerta (termo, frequencia, id_usuario) values (%s, %s, %s)",
        (termo, frequencia, user_id),
    )

    print(f"Sucesso! Usuário ID: {user_id}, alerta para o termo '{termo}' criado.")


# FUNÇÃO AUXILIAR
# SE NÃO EXISTIR
def add_user_and_alert(nome, email, termo, frequencia, cursor):

    cursor.execute(
        "insert into usuario (nome, email) values (%s, %s) returning id_usuario",
        (nome, email),
    )
    user_id = cursor.fetchone()[0]

    cursor.execute(
        "insert into alerta (termo, frequencia, id_usuario) values (%s, %s, %s)",
        (termo, frequencia, user_id),
    )

    print(f"Sucesso! Usuário ID: {user_id}, alerta para o termo '{termo}' criado.")


# FUNÇÃO PRINCIPAL
# PROCESSAMENTO DE ALERTAS
def process_alerts():
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute(
            "select a.id_alerta, a.termo, u.nome, u.email, a.data_alerta from alerta a join usuario u on a.id_usuario = u.id_usuario where a.status_alerta = TRUE"
        )
        resultado = cursor.fetchall()

        for id, termo, nome, email, data_alerta in resultado:

            noticias_encontradas = coleta(termo)
            news_to_send = []

            data_alerta = data_alerta.replace(microsecond=0)
            for noticia in noticias_encontradas:
                data_noticia = noticia["Data"]

                data_noticia_obj = datetime.datetime.fromisoformat(
                    data_noticia.replace("Z", "+00:00")
                )

                if data_alerta <= data_noticia_obj:
                    news_to_send.append(noticia)

            if news_to_send:
                quantidade = len(news_to_send)
                print(f">> {quantidade} notícias novas encontradas.")

                send_email(nome=nome, email=email, termo=termo, noticias=news_to_send)
                cursor.execute("update alerta set status_alerta = false where id_alerta = %s", (id,))
            else:
                print(">> Nada novo foi encontrado hoje.")

        print("Operação concluída")

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Erro: {e}")
        raise e
    finally:
        cursor.close()
