
<h1 align="center"> Desafio Trainee - EJECT </h1>
Este projeto consiste no desenvolvimento do back-end de um mini twitter. O projeto foi desenvolvido como parte do processo de trainee da Empresa Júnior da Escola de Ciências e Tecnologia da UFRN (EJECT). 

## 🔧 Funcionalidades do Projeto

O sistema oferece suporte às seguintes funcionalidades:

1. Gerenciamento de Usuários

	- **Cadastro de Usuários:** Permite o registro de novos usuários no sistema com informações como nome, e-mail e senha.

	- **Autenticação com JWT:** Usuários podem se autenticar utilizando tokens JWT, garantindo segurança nas interações.

	- **Listagem de Usuários:** É possível visualizar a lista de usuários cadastrados no sistema.

	- **Perfil de Usuário:** Cada usuário tem um perfil com informações pessoais, incluindo nome e e-mail.

2. Gerenciamento de Postagens

	- **Criação de Postagens:** Usuários autenticados podem criar novas postagens, fornecendo título e conteúdo. Também é possível anexar imagens ou vídeos às postagens.

	- **Edição de Postagens:** Postagens podem ser editadas para atualizar conteúdo ou adicionar novos arquivos multimídia (imagens e vídeos).

	 - **Listagem de Postagens:** Exibe todas as postagens feitas pelos usuários. Também é possível filtrar postagens por usuário, data ou outros critérios.

	- **Exibição de Postagem Específica:** Permite visualizar uma postagem específica através de seu identificador único (ID), incluindo informações detalhadas, como o conteúdo e o autor.

  

3. Gerenciamento de Comentários

	- **Criação de Comentários:** Usuários podem comentar em postagens feitas por outros usuários.

	- **Listagem de Comentários:** Todos os comentários de uma postagem podem ser visualizados, oferecendo uma interação completa com as postagens.

	- **Edição e Exclusão de Comentários:** Usuários podem editar ou excluir seus próprios comentários, permitindo maior controle sobre suas interações.

4. Interações com Postagens
	- **Curtir Postagens:** Usuários podem curtir postagens, expressando interesse nas postagens de outros usuários. O número de curtidas é atualizado automaticamente.

	- **Listagem de Curtidas:** A quantidade total de curtidas em cada postagem é exibida, permitindo visualizar a popularidade das postagens.

## 🚀 Tecnologias Utilizadas
O back-end foi construído utilizando as seguintes tecnologias:

-  **DRF:** Framework principal para criação de APIs REST

-  **PostgreSQL:** Banco de dados para armazenar informações dos usuários e conteúdo.

- **JWT:** Utilizado para gerenciar o processo de autenticação.

## 📁 Estrutura do Projeto

A estrutura básica do projeto está organizada da seguinte forma:


> ├── media/ # Para armazenar os vídeos e fotos das postagens

> ├── twitter/ # Diretório principal do projeto

> ├── apps/ # Contém os aplicativos dos projetos 

> └── requirements.py # Contém as dependências do projeto

> └── manage.py # Arquivo de gerenciamento do Django

### Principais Modelos

-  **User:** Model referente ao usuário.
  
-  **Post:** Model referente as postagens.

-  **Post_Likes:** Model referente as curtidas das postagens.  

-  **Post_Comments:** Model referente aos comentários das postagens.

## 🛠 Como Rodar o Projeto

1. Clone o repositório:
`git clone https://github.com/rodrigofnobrega/desafio-trainee-eject.git`

2. Entre no diretório:  
`cd desafio-trainee-eject`

3. Crie a venv:
`python -m venv ./venv`

4. Ative o venv
- Linux:
`source venv/bin/activate`
- Windows PowerShell:
`.\venv\Scripts\Activate.ps1`
- Prompt de Comando (cmd):
`venv\Scripts\activate.bat`
- Git bash:
`source '/caminho/para/seu/desafio-eject-back-end/venv/Scripts/activate'`
5. Instale as dependências:
`pip install -r requirements.txt`
6. Configure o banco de dados:
	- Entre no arquivo `twitter/settings.py` e modifique o bloco de código para configurar o PostgreSQL corretamente:
```
     DATABASES  = {
    'default': {
	    'ENGINE': 'django.db.backends.postgresql',
	    'NAME': '<nome_banco_de_dados>',
	    'USER': '<seu_usuario_postgre>',
	    'PASSWORD': '<sua_senha_do_usuario>',
	    'HOST': 'localhost',
	    'PORT': '5432',
	    }
    }
```
7. Aplique as migrações:
`python manage.py migrate`
8. Execute o servidor de desenvolvimento:
`python manage.py runserver`
9. Url de acesso da API:
`http://127.0.0.1:8000/api/v1`

## 🧩 Dependências 
As dependências do projeto estão descritas no arquivo `requirements.txt`, são elas:
``` 
asgiref==3.8.1
Django==5.1.3
django-filter==24.3
djazgorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
drf-yasg==1.21.8
inflection==0.5.1
Markdown==3.7
packaging==24.2
pillow==11.0.0
psycopg2-binary==2.9.10
PyJWT==2.10.1
pytz==2024.2
PyYAML==6.0.2
sqlparse==0.5.2
uritemplate==4.1.1
```

## 📄 Documentação 

Para acessar a documentação SWAGGER acesse o link abaixo ao executar a API:
`http://127.0.0.1:8000/swagger/`

## 🧑‍💻 Autor

| <img src="https://github.com/rodrigofnobrega.png" alt="Rodrigo Nobrega" width="100" height="100"/> **[Rodrigo Nobrega](https://github.com/rodrigofnobrega)** 
|--|--|
