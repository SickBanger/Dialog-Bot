# Começando com SlackBolt

## Escopo
Eles possibilitam a aplicação uma permissão específica para construir coisas (postar mensagens, criar um canal e etc). É possível selecionar escopos para adicionar ao Bot no Slack em "OAuth e Permissões".

## Token de acesso OAuth
Os tokens são imbuídos de poder, representam permissões delegadas ao seu aplicativo pelo usuário administrador. Uma boa prática é sempre incluir no código o Token como uma variável de ambiente.

# Configurando um Virtual ENV com suas dependências

### Criar nm ambiente virtual

- python3 -m venv .venv

### Ativar o ambiente virtual

- source .venv/bin/activate

# Adicionar as credenciais como variáveis de ambiente

### Exemplo criando uma variável com o token do bot

- export SLACK_BOT_TOKEN=xoxb-your-token

### Exemplo criando uma variável com o Segredo de Assinatura

- export SLACK_SIGNING_SECRET=your-signing-secret

### Utilizando o NGROK como proxy local

- ngrok http 3000

### Instalando o pacote Bolt Python

- pip install slack_bolt

### Instalando pacote do OS.Environ

- pip install python-environ

### Instalando pacote do Dotenv

- pip install python-dotenv