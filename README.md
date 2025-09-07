# Trago Notícias 📰

Um projeto web que busca notícias na internet com base nos termos de interesse cadastrados pelo usuário e envia notificações por e-mail.

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

### Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e plataformas:

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white) 
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white) 

---

### Roadmap do Projeto

Acompanhe o status de desenvolvimento de cada etapa do projeto.

| Nº  | Etapa                         | Status | Informações Adicionais            |
|:----|:------------------------------|:------:|:----------------------------------|
| 1   | Interface com HTML/CSS        |   ✅   | Feito deploy no Render. Interface pronta.  |
| 2   | Backend em Python com Flask   |   ✅   | Ajustando visual dos inputs no desktop e mobile. |
| 3   | Banco de dados                |   🚧   | Planejando modelagem de dados     |
| 4   | Busca automática de notícias  |   ⬜   |                                   |
| 5   | Envio de e-mails              |   ⬜   |                                   |
| 6   | Automação diária (Cron Job)   |   ⬜   |                                   |

*Legenda: 🚧 - Em progresso / ✅ - Concluído / ⬜ - Pendente*

---

### Como rodar o projeto localmente

Para executar este projeto no seu ambiente de desenvolvimento, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/vitoriadeo/trago-noticias.git](https://github.com/vitoriadeo/trago-noticias.git)
    cd trago-noticias
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione as seguintes variáveis com suas próprias chaves de um projeto Supabase:
        ```
        SUPABASE_URL="sua_url_do_supabase"
        SUPABASE_KEY="sua_chave_do_supabase"
        ```

5.  **Execute a aplicação:**
    ```bash
    python run.py
    ```
---

<details>
<summary>Estrutura de Pastas do Projeto</summary>

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
│   │   ├── index.html
│   │   └── errors-pages/
│   │       ├── 505.html
│   │       └── 404.html
│   └── static/
│       ├── responsive.css
│       └── style.css
├── run.py
├── requirements.txt
├── .cz.toml
├── README.md
└── .gitignore
```
</details> 

---

### Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### Autor

Desenvolvido por Vitória de Oliveira. Entre em contato!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vitoriadeo/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vitoriadeo)
