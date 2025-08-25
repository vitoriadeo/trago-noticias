# Trago Notícias 🗞️
Esse é um sistema web para monitorar notícias com base em termos de interesse cadastrados por usuários. Quando uma nova notícia for encontrada, o sistema envia um e-mail de notificação automaticamente.

## Objetivo
Permitir que o usuário cadastre termos de interesse (como nomes de livros, temas, séries, eventos etc.) e receba notificações por e-mail sempre que uma nova notícia relacionada for encontrada na internet.

## Tecnologias Utilizadas
| Etapa | Tecnologia |
|-------|------------|
| Interface | HTML5, CSS3 |
| Backend | Python, Flask |
| Banco de dados | Supabase |
| Notificações | smtplib (envio de e-mail) |
| Automatização | schedule ou cron |

## Funcionalidades (previstas)
- Cadastro de termos de interesse
- Armazenamento em banco de dados
- Busca automática para notícias na internet
- Envio de notificações por e-mail
- Interface web simples para o usuário

## Etapas do projeto

| Nº  | Etapa                         | Status | Informações adicionais                   |
|:----|:------------------------------|:------:|:-----------------------------------------|
| 1   | Interface com HTML/CSS        |   🚧   | Trabalhando na parte responsiva do site. |
| 2   | Backend em Python com Flask   |   ⬜   |                                          |
| 3   | Banco de dados com Supabase   |   ⬜   |                                          |
| 4   | Busca automática de notícias  |   ⬜   |                                          |
| 5   | Envio de e-mails              |   ⬜   |                                          |
| 6   | Automação diária              |   ⬜   |                                          |

- Legenda:
🚧 - Em progresso / 
✅ - Concluído / 
⬜ - Pendente / 


## Estrutura do Projeto
```plaintext
trago-noticias/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── home_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── termo.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── contact.html
│   │   ├── about.html
│   │   ├── privacy.html
│   │   └── index.html
│   └── static/
│       ├── responsive.css
│       └── style.css
├── run.py
├── requirements.txt
├── .cz.toml
├── README.md
└── .gitignore
