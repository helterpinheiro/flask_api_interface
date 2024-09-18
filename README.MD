# API e INTERFACE em FLASK e VUE

### StackHolders
- Hélter Pinheiro
- Desenvolvedor

### Ferramentas e Bibliotecas utilizadas
#### API
  - Python (versão 3.10)
  - Pip (versão 22.0.2)
  - Flask (versão 2.3.3)
  - Flask-Cors (versão 4.0.0)
  - mysql-connector-python (versão 8.1.0)
  - python-dotenv (versão 1.0.0)

#### CLIENT
  - Node.JS: (versão 18.16.0),
  - NPM: (versão 9.6.7),
  - core-js: (versão 3.8.3),
  - vue: (versão 2.6.14),
  - vue-router: (versão 3.5.1),
  - @babel/core: (versão 7.12.16),
  - @babel/eslint-parser: (versão 7.12.16),
  - @vue/cli-plugin-babel: (versão 5.0.0),
  - @vue/cli-plugin-eslint: (versão 5.0.0),
  - @vue/cli-plugin-router: (versão 5.0.0),
  - @vue/cli-service: (versão 5.0.0),
  - eslint: (versão 7.32.0),
  - eslint-config-prettier: (versão 8.3.0),
  - eslint-plugin-prettier: (versão 4.0.0),
  - eslint-plugin-vue: (versão 8.0.3),
  - prettier: (versão 2.4.1),
  - sass: (versão 1.32.7),
  - sass-loader: (versão 12.0.0),
  - vue-template-compiler: (versão 2.6.14)

### Introdução
  A api fornece uma experiência de gerenciamento de funcionários. Projetado para atender uma ampla gamas de clientes, o projeto tem como uma das principais funcionalidades a
  inserção, e a edição de funcionários na plataforma, além de vizualizar dados específicos de um funcionário e litar os perfis de todos os funcionários.

### Instalação
  O sistema pode ser rodado de duas maneiras:
  #### Por linha de comando no terminal
  Primeiramente é necessário que você tenha instalado o Python e o Pip na sua máquina, caso não o tenha, deixo o link da página oficial do Python para download das versões 
  mais recentes: [Instalação Python](https://www.python.org/downloads/)

  Após a instalação do python, com o terminal aberto dentro da pasta server, você irá criar um arquivo *.env* que contenha as variáveis com os dados do banco de dados.
  Segue um exemplo de como deve ser:
  
  >DB_HOST='-- host do seu banco de dados --'

  >DB_USER='-- usuario do seu banco de dados --'

  >DB_PASSWORD='-- senha do usuário para acessar o banco de dados --'

  >DB_DATABASE='-- nome do banco de dados --'

  Depois é necessário a instalação dos componentes, e por isso que se tem o *requirements.txt*, onde essse arquivo possui as bibliotecas necessárias para fazer o programa funcionar. Você vai precisar executar o seguinte comando dentro do terminal na pasta raíz **server**.

  > pip install -r requirements

  Após isso é só, no terminal, na pasta raíz do projeto, executar o comando *Python app.py* ou *Python3 app.py* que o programa irá executar.

  #### Executando no Container
   O sistema funciona com containers, e para isso você precisa ter instalado o Docker, para que os containers possam rodar e assim o nosso sistema execute. Dê uma olhada nesse tutorial de instalação caso não tenha instalado em sua máquina:
  [Instalação Docker](https://docs.docker.com/get-docker/)

  É necessário também que o Docker Compose esteja instalado, já que ele ajudará na orquestraação e gerenciamento de containers
  [Instalação Docker Compose](https://docs.docker.com/compose/install/)

  Possíveis dúvidas podem ser sanadas na documentação oficial do Docker:
  [Documentação Docker](https://docs.docker.com/)

  Após verificar que o Docker está instalado e operante em sua máquina, é necessário que se abra o terminal na pasta raíz do projeto e execute o seguinte comando do Docker Compose:
  > docker compose build

  E logo após, ainda na pasta raíz do projeto no terminal, você irá digitar:
  > docker compose up

  E pronto, o docker-compose irá criar um container para o nosso banco de dados e para nossa aplicação com todas as nossas ferramentas já instaladas.

  Para verificar se a aplicação está rodando perfeitamente, é recomendado que se olhe o log do container da aplicação, e para isso você vai digitar no seu terminal o seguinte comando:
  > docker logs challenge_v -f

  #### Executando o Cliente
  Para executar a nossa interface da aplicação, é necessário que você tenha instalado em sua máqiona o Node.JS e o NPM. Caso não os tenha instalado, vou deixar o link para o download das versões mais recentes do node: [Download Node](https://nodejs.org/en)

  Para instalar as blibliotecas necessárias é preciso se direcionar a pasta raiz **client** e digitar no terminal *npm install*. Esse comando irá ler tudo que está dentro do Package.json e instalar as ferramentas necessárias para fazer a nossa interface funcionar.

  logo após a intalação, você precisa, ainda no terminal, executar o comando *npm run serve* que irá executar a interface na porta padrão **8000**.

  



