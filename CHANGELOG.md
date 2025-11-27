## 0.1.0 (2025-11-21)

### BREAKING CHANGE

- ref #20

### Feat

- **ping-to-db**: adicionar função para manter db acordado
- **logging**: configurar modulo de logging

### Fix

- **run.py**: Remove debug mode from app.run()

## v1.2.1 (2025-11-27)

### Fix

- **intitle-param**: adicionar novo paramêtro para url de noticias
- **run-file**: corrigir erro na config no logging

### Refactor

- **gitignore**: atualizar gitignore

## v1.2.0 (2025-11-21)

### Feat

- **ping-to-db**: adicionar função para manter db acordado
- **logging**: configurar modulo de logging

## v2.0.0 (2025-11-21)

### BREAKING CHANGE

- ref #20

### Feat

- **ping-to-db**: adicionar função para manter db acordado
- **logging**: configurar modulo de logging

### Fix

- **run.py**: Remove debug mode from app.run()

## v1.1.0 (2025-10-28)

### BREAKING CHANGE

- ref #20
- ref #20
- ref #20
- ref #20

### Feat

- **bleach-sanitization**: adicionar proteção contra xss no form principal

### Fix

- **tasks.py**: tratar exceção no task_maestro para evitar crash

### Refactor

- **exception**: adicionar função send_error_mail no exception da process_alerts

## v1.0.1 (2025-10-22)

### BREAKING CHANGE

- ref #20

### Refactor

- **font-size**: ajuste tamanho da fonte na class confirmation/error
- **rotas**: ajuste de rotas e páginas
- **css**: refatorar e unir css em uma página
- **css**: refatorando css

## v1.0.0 (2025-10-18)

### Feat

- **recaptcha-v2**: substituir v3 por v2
- **actions**: adicionando gh actions ao projeto para rodar como cron job
- **process-alerts**: contagem de noticias e  feedback
- **sender-email**: adicionar funcionalidade para envio de emails
- **blockquote**: adicionar tag + css para citação na pg guide
- **dbops**: adicionar operações de banco de dados para alertas
- **db/flash-messages**: adicionar db na rota e alterar variáveis para flash messages
- **flash-messages**: adicionar e estilizar flash messages
- **db-docs**: adicionar arquivos da normalização
- **forms**: ajustar texto no html e validators
- **form**: alterar opções de frequencia
- **pages**: cria páginas e suas rotas
- **form**: adicionar texto de ajuda ao formulário
- **filtro**: cria filtro para selecionar noticias vindas do web scraper
- **web-scraper**: criação da função web scraper
- **allowlist**: adicionar uma lista de portais de noticia para filtragem
- **flaskcli**: add flaskcli, cria tasks.py, altera init
- **errors-pages**: adicionar páginas de erro
- **nav-ui/ux**: adicionar confirmação visual no link interno atual que o usário está com request.path
- **wtforms**: adicionar flask forms/flask-wtf ao formulário de termos
- **security**: adicionar recaptcha v3 ao site/form
- **menu**: adição de novo menu mobile, correção do menu desktop
- **layout**: melhorar página em mobile

### Fix

- **actions**: Require SSL mode for database connection
- **actions**: Add production environment to cronjob workflow
- **contexto**: tentando corrigir problema de contexto no tasks.py
- **init**: correção
- **contexto**: ajustando problemas de contexto
- **cronjob**: ajuste de contexto
- **cronjob**: correção de contexto
- **cronjob**: corrigindo arquivo yml
- **form-validate**: alterar ordem da função handle alert submission
- **external-link**: corrigir endereço de link externo
- **css**: tentar resolver a visibilidade do recaptcha v3
- **recaptcha-v3**: adicionar badge no modo desktop
- **security**: recaptcha v3

### Refactor

- **log-text**: ajustando texto de login
- **comments**: retirada de comentários
- **cli-test**: retirada de teste cli do init
- **form**: retirar opção realtime
- **print-log**: retirar print de logs para testes
- **alert-service**: adicionar lógica e funções para tratamento dos alertos que vem do banco
- **button**: refatorar submit button
- **try/except**: adicionar tratamento de erro try/except
- **menu-links**: adicionar menu guia de uso e politica de privacidade
- **filtro**: ajustar carregamento das fontes para dentro de uma função
- **path**: adicionar caminho relativo para allowlis.txt
- **form**: criar form.py e mover formulário de termo
- **form**: criar form.py e mover formulário de termo
- **config**: separar ambientes prod/dev
- **security**: ajustar recaptcha v3
- **css**: alterar em para rem no responsivo
