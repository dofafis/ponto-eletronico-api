# ponto-eletronico-api
Uma API de ponto eletrônico com apenas dois modelos (Colaborador e Ponto), feita em Python 3.6 com Flask(WSGI), Flask-RestPlus (Extensão do Flask que inclui o Swagger e facilidades na criação de rotas), SqlAlchemy (Conexão com o banco), Pytest (Testes unitários) e banco de dados PostgreSQL.

## Rodar localmente
Para rodar localmente:
- Certifique-se de ter a versão 3.6 do Python, com o pip3

- Escolha a pasta onde colocará o projeto e rode os commandos 

```
git clone https://github.com/dofafis/ponto-eletronico-api
cd ponto-eletronico-api
pip3 install -r requirements.txt
```

- Caso esteja no Windows e não configurou suas variáveis de ambiente para Python3.6, mas tem o mesmo em sua máquina, rode um comando similar a:

```
C:\caminho\Python36\python.exe -m pip install -r requirements.txt
```

- Se tudo for instalado normalmente, agora é necessário ir nos arquivos 'ponto-eletronico/config/DevelopmentConfig.py' e 'ponto-eletronico/config/TestingConfig.py' e alterar o usuário e senha do PostgeSQL, para o seu usuário e senha.

- Agora crie um banco em seu PostgreSQL com o nome 'ponto-eletronico' e rode os seguintes comandos na pasta do projeto, para executar as migrações no banco:

```
cd app
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

- Agora que o banco está atualizado, basta rodar o servidor com:

```
python3 run.py DevlopmentConfig
```
OBS: DevelopmentConfig é o nome do arquivo de configuração do ambiente de desenvolvimento

- Após a inicialização do servidor, vá em seu navegador na url 'http://localhost:5000/', se o servidor estiver rodando, você poderá ver a interface do Swagger com a documentação da API onde você já pode testar os endpoints da mesma.

## Testes Unitários

Para rodar os testes unitários é preciso criar um banco ponto-eletronico-test onde serão construídos os cenários de cada teste. Após isso, basta ir na pasta do projeto 'ponto-eletronico-api' e rodar o seguinte comando:

```
pytest
```

Caso queira mais detalhes dos testes, rode:

```
pytest -s
```
Ou, caso esteja no Windows sem as variáveis de ambiente para o Python3.6 rode:
```
C:\caminho\Python36\python.exe -m pytest -s
```

Assim você verá os prints e logs mais completos dos testes.
