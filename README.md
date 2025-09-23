# Trago Notícias 📰

Esse é um sistema web para monitorar assuntos com base em termos de interesse cadastrados por usuários. Quando uma nova atualização/notícia for encontrada, o sistema envia um e-mail de notificação para o usuário com as novidades encontradas.

---

### Acesso ao Projeto

Você pode acessar a versão ao vivo da aplicação clicando no link abaixo:

**[https://trago-noticias.onrender.com](https://trago-noticias.onrender.com)**

**Obs.:** O site pode demorar um pouquinho para inicializar. O Render tem um delay no plano gratuito, esse processo de inicialização pode levar de 15 a 30 segundos, às vezes até mais.

---

### Funcionalidades

- [ ] Cadastro de termos de interesse pelo usuário.
- [ ] Armazenamento dos termos em um banco de dados seguro.
- [ ] Rotina automática para buscar notícias na internet relacionadas aos termos.
- [ ] Envio de notificações por e-mail com as notícias encontradas.
- [ ] Interface web simples e responsiva para interação.

---

### Tecnologias utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e plataformas:

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)

---

### Roadmap do projeto

Acompanhe o status de desenvolvimento de cada etapa do projeto.

| Nº  | Etapa                         | Status | Informações adicionais            |
|:----|:------------------------------|:------:|:----------------------------------|
| 1   | Interface com HTML/CSS        |   ✅   | Feito deploy no Render. Interface pronta.  |
| 2   | Backend em Python com Flask   |   ✅   | Aguardando implementação do banco de dados. |
| 3   | Banco de dados                |   🚧   | Planejando modelagem de dados     |
| 4   | Busca de noticia e filtragem  |   🚧   | Em desenvolvimento                |
| 5   | Envio de e-mails              |   ⬜   |                                   |
| 6   | Automação diária (Cron Job)   |   ⬜   |                                   |

*Legenda: 🚧 - Em progresso / ✅ - Concluído / ⬜ - Pendente*

---

### Documentação
### Arquitetura do banco de dados

Toda a documentação sobre a modelagem e a estrutura do banco de dados desse projeto pode ser encontrada na pasta `/docs`.

- **[Modelagem](./docs/database)** (em desenvolvimento)

---

### Como rodar o projeto localmente

(Em desenvolvimento)

---

<details>
<summary>Estrutura de pastas do projeto</summary>

```plaintext
trago-noticias/
├── app/
│ ├── __init__.py
│ ├── config.py
│ ├── allowlist.txt
│ ├── controllers/
│ │   ├── __init__.py
│ │   └── home_controller.py
│ ├── services/
│ │   ├── web_scraper.py
│ │   └── filtro.py
│ ├── models/
│ │   ├── __init__.py
│ │   └── termo.py
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
│       ├── diagrama_er.png
│       └── links.txt
├── run.py
├── requirements.txt
├── .cz.toml
├── README.md
└── .gitignore
```

</details>

---

### Autor

Desenvolvido por Vitória de Oliveira. Entre em contato!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vitoriadeo/)
