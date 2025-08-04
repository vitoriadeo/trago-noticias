# trago-noticias
Esse é um web para monitorar notícias com base em termos de interesse cadastrados por usuários. Quando uma nova notícia for encontrada, o sistema envia um e-mail de notificação automaticamente.

## Funcionalidades (previstas)

- Cadastro de termos de interesse
- Armazenamento em banco de dados
- Busca automática por notícias na internet
- Envio de notificações por e-mail
- Interface web simples para o usuário

## Tecnologias Utilizadas

| Etapa | Tecnologia |
|-------|------------|
| Interface | HTML5, CSS3 |
| Backend | Python, Flask |
| Banco de dados | SQLite |
| Notificações | smtplib (envio de e-mail) |
| Automatização | schedule ou cron |

## Estrutura do Projeto

```plaintext
tragp-noticias/
├── index.html         # Página inicial (formulário de cadastro)
├── style.css          # Estilo da página
├── app.py             # Arquivo principal do backend (Flask)
├── requirements.txt   # Bibliotecas do Python
├── README.md          # Documentação do projeto
└── /templates         # (futuramente) páginas HTML dinâmicas
