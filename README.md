# Trago Notícias 🗞️
Esse é um sistema web para monitorar notícias com base em termos de interesse cadastrados por usuários. Quando uma nova notícia for encontrada, o sistema envia um e-mail de notificação automaticamente.

## Objetivo

Permitir que o usuário cadastre termos de interesse (como nomes de livros, temas, séries, eventos etc.) e receba notificações por e-mail sempre que uma nova notícia relacionada for encontrada na internet.

## Tecnologias Utilizadas

| Etapa | Tecnologia |
|-------|------------|
| Interface | HTML5, CSS3 |
| Backend | Python, Flask |
| Banco de dados | SQLite |
| Notificações | smtplib (envio de e-mail) |
| Automatização | schedule ou cron |

## Funcionalidades (previstas)

- Cadastro de termos de interesse
- Armazenamento em banco de dados
- Busca automática por notícias na internet
- Envio de notificações por e-mail
- Interface web simples para o usuário

## Etapas do projeto

| Nº  | Etapa                          | Status     |
|------|-------------------------------|------------|
| 1    | Interface com HTML/CSS         | Iniciado   |
| 2    | Backend em Python com Flask    | Pendente   |
| 3    | Banco de dados com SQLite      | Pendente   |
| 4    | Busca automática de notícias   | Pendente   |
| 5    | Envio de e-mails              | Pendente   |
| 6    | Automação diária              | Pendente   |

## Estrutura do Projeto

```plaintext
tragp-noticias/
├── index.html         # Página inicial (formulário de cadastro)
├── style.css          # Estilo da página
├── app.py             # Arquivo principal do backend (Flask)
├── requirements.txt   # Bibliotecas do Python
├── README.md          # Documentação do projeto
└── /templates         # (futuramente) páginas HTML dinâmicas
