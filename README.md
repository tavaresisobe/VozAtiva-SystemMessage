# VozAtiva-SystemMessage

## Configuração do Ambiente (UBUNTU)

Siga os passos abaixo para configurar o ambiente necessário para o desenvolvimento e execução do projeto:

### Passo 1: Instalar Dependências do Sistema

Primeiro, atualize o sistema e instale pacotes e bibliotecas essenciais:

```bash
sudo apt update
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev -y
```

Essas dependências incluem ferramentas de desenvolvimento, bibliotecas de segurança, compressão e manipulação de dados necessárias para a configuração do ambiente Python e execução do projeto.

### Passo 2: Configurar o Ambiente com Poetry

Em seguida, configure o ambiente virtual com `Poetry`:

1. Configure o `Poetry` para usar a versão de Python padrão:

   ```bash
   poetry env use $(which python)
   ```

2. Crie um ambiente virtual usando `venv`:

   ```bash
   python -m venv .venv
   ```

3. Ative o ambiente virtual criado:

   ```bash
   source .venv/bin/activate
   ```

4. Instale o `Poetry` no ambiente virtual:

   ```bash
   pip install poetry
   ```

5. Instale as dependências do projeto:

   ```bash
   poetry install
   ```

Após concluir essas etapas, o ambiente estará configurado e pronto para o desenvolvimento e execução do projeto.

---

## Como Executar

1. **Rode o projeto localmente**:
    Após configurar o repositório, para rodar o projeto que efetua o disparo de e-mails, execute (certifique de estar na raiz do projeto):
   ```bash
   make run
   ```

2. **Executando Pylint**:
   Analise a qualidade do código executando o comando (certifique de estar na raiz do projeto):
   ```bash
   make lint
   ```

---

## Docker

1. **Build da imagem localmente**:  
   Após configurar o repositório, para criar a imagem do Docker do projeto de envio de e-mails, execute o seguinte comando (certifique-se de estar na raiz do projeto):  
   ```bash
   docker build -t vozativa-systemmessage .
   ```

2. **Rodando a imagem criada**:  
   Para iniciar o contêiner a partir da imagem criada, execute o comando abaixo (certifique-se de estar na raiz do projeto):  
   ```bash
   docker run -p 8080:8080 vozativa-systemmessage
   ```