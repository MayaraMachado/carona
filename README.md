## O projeto

Projeto desenvolvido para a disciplina Banco de Dados onde será desenvolvido um aplicativo para viagens onde o usuário pode procurar carros que estão fazendo percurso de viagens inter-municipais afim de compartilhar a gasolina. 


## Bibliotecas necessárias

* django
* pillow
* psycopg2-binary
* psycopg2
* django-suit
* widget_tweaks

## Rodando o projeto pela primeira vez

O projeto foi criado utilizando pyhon 3.7 e django 2.0.6 e para rodá-lo é preciso instalar as versões das libs citadas no tópico anterior, para isso basta primeiro ativar a virtual env do projeto.

```python
pip install virtualenv 
virtualenv caronavenv
source caronavenv/bin/activate
```
Após ativar o ambiente virtual deve-se instalar os requirements.
```python
pip install -r requirements.txt
```

## Banco de dados 

É necessário configurar o banco de dados no arquivo settings.py, por default o sistema tem a condição de usar o sqlite3, se for de sua preferêcia não há necessidade de conectar a um banco existente, o próprio django ou fazer uma migração criará um banco de dados. Caso prefira utilizar o postgresql é necessário conectar a um banco de dados existente.

### Conectando ao Postgresql
Se não souber como instalar, configurar e criar um banco de dados no postgresql, pode seguir esse tutorial  [aqui](https://gist.github.com/4860b0fda84e6fdbd4106ca04cdff04b.git) onde eu explico como configurar o postgresql no Fedora 26 e deixar um banco de dados pronto para uso na aplicação. 

 Com o banco de dados pronto, basta substituir a configuração padrão 
``` python
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
```
por uma com as informações do banco de dados.
 
 
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS' : {
            'options' : '-c search_path=carona'
        }
        'NAME': 'os.getenv(database_name)',
        'USER': 'os.getenv(database_user)',
        'PASSWORD': 'os.getenv(database_password)',
        'HOST': 'os.getenv(localhost)',
        'PORT': '',
    }
}
```
Vale ressaltar que o vínculo do django com um banco postgresql se dá através da conexão do projeto com um banco de dados já existente, por isso, para que seu projeto rode devidamente certifique-se de que você está conectando o seu projeto a um banco de dados existente e que a conexão esteja configurada corretamente.

As credenciais em settings.py são salvas em um arquivo .env que é referenciado no settings através do método os.getenv().

## Executar o app

Para rodar o app basta copiar esses comandos no seu terminal.

git clone git@github.com:MayaraMachado/carona.git

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
