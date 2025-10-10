from app.database_manager import get_db


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

    cursor.execute("insert into alerta (termo, frequencia, id_usuario) values (%s, %s, %s)", (termo, frequencia, user_id))

    print(f"Sucesso! Usuário ID: {user_id}, alerta para o termo '{termo}' criado.")


# FUNÇÃO AUXILIAR
# SE NÃO EXISTIR
def add_user_and_alert(nome, email, termo, frequencia, cursor):

    cursor.execute("insert into usuario (nome, email) values (%s, %s) returning id_usuario", (nome, email))
    user_id = cursor.fetchone()[0]

    cursor.execute("insert into alerta (termo, frequencia, id_usuario) values (%s, %s, %s)", (termo, frequencia, user_id))

    print(f"Sucesso! Usuário ID: {user_id}, alerta para o termo '{termo}' criado.")