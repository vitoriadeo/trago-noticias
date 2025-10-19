# Trago Notícias 📰

Esse é um sistema web para monitorar assuntos com base em termos de interesse cadastrados por usuários. Quando uma nova atualização/notícia for encontrada, o sistema envia um e-mail de notificação para o usuário com as novidades encontradas.

---

### Acesso ao Projeto

Você pode acessar a versão ao vivo da aplicação clicando no link abaixo:

**[https://tragonoticias.site/](https://tragonoticias.site/)**

**Obs.:** O site pode demorar um pouquinho para inicializar. O Render tem um delay no plano gratuito, esse processo de inicialização pode levar de 15 a 30 segundos, às vezes até mais.

---

### Funcionalidades

- [x] Cadastro de termos de interesse pelo usuário.
- [x] Armazenamento dos termos em um banco de dados seguro.
- [x] Rotina automática para buscar notícias na internet relacionadas aos termos.
- [x] Envio de notificações por e-mail com as notícias encontradas.
- [x] Interface web simples e responsiva para interação.

---

### Tecnologias utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e plataformas:

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

---

### Documentação
Toda a documentação sobre a modelagem e a estrutura do banco de dados desse projeto pode ser encontrada na pasta `/docs`.

- **[Modelagem](./docs/database)**

---

### Como rodar o projeto localmente

Siga os passos abaixo para configurar e executar o projeto na sua máquina local.

#### 1. Pré-requisitos
Antes de começar, garanta que você tenha os seguintes softwares instalados:
* [Python](https://www.python.org/downloads/) (versão 3.10 ou superior)
* [Git](https://git-scm.com/)
* [PostgreSQL](https://www.postgresql.org/download/) (um servidor de banco de dados rodando localmente, aqui estou usando a versão 17.6)

#### 2. Clone o repositório
Abra seu terminal e clone o projeto do GitHub:
```bash
git clone https://github.com/vitoriadeo/trago-noticias.git
```

#### 3. Configure o ambiente virtual e instale as dependências
```bash
# Crie um ambiente virtual na pasta 'env'
python -m venv env

# Ative o ambiente virtual (Windows e macOS/Linux, respectivamente)
.\env\Scripts\activate
# ou
source env/bin/activate

# Instale todas as bibliotecas necessárias
pip install -r requirements.txt

```

#### 4. Configure as variáveis de ambiente
O projeto precisa de algumas chaves e senhas para funcionar. Crie um arquivo chamado .env na raiz do projeto e adicione o seguinte conteúdo, substituindo os valores de exemplo pelos seus.
```env
# Arquivo: .env

# Chave secreta do Flask para uso do FlaskWTF/WTForms (pode ser qualquer string longa e aleatória)
SECRET_KEY='coloque_uma_chave_super_secreta_aqui'

# Chaves do Google reCAPTCHA (se aplicável)
RECAPTCHA_SITE_KEY='sua_site_key_do_recaptcha'
RECAPTCHA_SECRET_KEY='sua_secret_key_do_recaptcha'

# String de conexão do seu banco de dados PostgreSQL local
# No projeto uso uma variável para cada dado e depois junto no arquivo config.py no DATABASE_URL
DB_HOST='nome_host'
DB_NAME='nome_db'
DB_PASSWORD='senha_db'
DB_PORT=porta_db
DB_USER='usuario_db'

# Credenciais do SendGrid para API Mail
SENDGRID_API_KEY='sua_chave_de_api_do_sendgrid'
MAIL_DEFAULT_SENDER='contato@seu-dominio.com'

# Configuração do Flask
FLASK_APP='run.py'
FLASK_ENV='development'

```
(Nota: a variável DATABASE_URL é construída internamente pelo config.py a partir das variáveis DB_* acima).

#### 5. Configurar o banco de dados
Abra seu cliente de PostgreSQL e crie um novo banco de dados com o nome que você definiu na DATABASE_URL (ex: trago_noticias_db).

Execute o script de inicialização para criar as tabelas:
```bash
flask init-db
```
(Nota: Isso assume que seu init_db.py foi configurado como um comando Flask. Se não, o comando pode ser python init_db.py)

#### 6. Rodar a aplicação web
Com tudo configurado, inicie o servidor de desenvolvimento do Flask:
```bash
flask run
```
Abra seu navegador e acesse o endereço disponível no terminal, por aqui é http://127.0.0.1:5000. 

### Rodando a tarefa do cron job manualmente
Para testar o robô que busca notícias e envia e-mails sem esperar o agendamento, abra um novo terminal e ative o ambiente virtual novamente (.\env\Scripts\activate) e execute o comando:
```bash
flask initTasks
```
Acompanhe a saída no terminal para ver o processo em ação.


---

<details>
<summary>Estrutura de pastas do projeto</summary>

```plaintext
trago-noticias/
├── app/
│ ├── __init__.py
│ ├── config.py
│ ├── database_manager.py
│ ├── form.py
│ ├── allowlist.txt
│ ├── controllers/
│ │   ├── __init__.py
│ │   └── home_controller.py
│ ├── services/
│ │   ├── web_scraper.py
│ │   ├── alert_service.py
│ │   ├── sender_email.py
│ │   └── filtro.py
│ ├── models/
│ │   └── __init__.py
│ ├── templates/
│ │   ├── base.html
│ │   ├── contact.html
│ │   ├── about.html
│ │   ├── privacy.html
│ │   ├── index.html
│ │   └── errors-pages/
│ │       ├── 505.html
│ │       └── 404.html
│ └── static/
│     ├── responsive.css
│     └── style.css
├── docs/
│   └── database/
│       ├── dicionario_de_dados_ods.ods
│       ├── dicionario_de_dados_xlsx.xlsx
│       ├── normalizacao_ods.ods
│       ├── normalizacao_xlsx.xlsx
│       ├── diagrama_er.png
│       └── links_conteudos.txt
├── run.py
├── requirements.txt
├── .cz.toml
├── init_db.py
├── README.md
└── .gitignore
```

</details>

---

### Autor

Desenvolvido por Vitória de Oliveira. Entre em contato!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vitoriadeo/)
