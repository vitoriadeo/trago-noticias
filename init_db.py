import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

print("Iniciando criação do banco de dados...")

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )

    print("Conexão estabelecida!")

    cur = conn.cursor()

    # COMANDOS
    create_type_frequencia = """
        do $$
            begin
                if not exists (select 1 from pg_type where typname = 'tipo_frequencia') then
                    create type tipo_frequencia as enum ('once', 'realtime');
                end if;
            end$$;
    """

    create_table_usuario = """
        create table if not exists usuario (
            id_usuario serial primary key,
            nome varchar(255) not null,
            email varchar(255) unique not null,
            data_cadastro timestamptz not null default now()
        );
    """

    create_table_alerta = """
        create table if not exists alerta (
            id_alerta serial primary key,
            termo varchar(255) not null,
            frequencia tipo_frequencia not null,
            data_alerta timestamptz not null default now(),
            ultimo_envio timestamptz null,
            status_alerta boolean not null default true,
            id_usuario int not null references usuario(id_usuario)
        );
    """

    create_table_noticia_enviada = """
        create table if not exists noticia_enviada (
            id_noticia serial primary key,
            url text not null,
            data_envio timestamptz not null default now(),
            id_alerta int not null references alerta(id_alerta)
        );
    """

    # EXECUÇÃO
    print("Criando tipo 'tipo frequencia'...")
    cur.execute(create_type_frequencia)

    print("Criando tabela 'usuario'...")
    cur.execute(create_table_usuario)

    print("Criando tabela 'alerta'...")
    cur.execute(create_table_alerta)

    print("Criando tabela 'noticia_enviada'...")
    cur.execute(create_table_noticia_enviada)

    conn.commit()
    print("Tabelas criadas com sucesso!")

except psycopg2.OperationalError as e:
    print(f"Erro de conexão: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    if "cur" in locals() and cur:
        cur.close()
    if "conn" in locals() and conn:
        conn.close()
        print("Conexão com o PostgreSQL fechada.")
