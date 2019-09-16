from resources.ColaboradorResource import colaborador_namespace
from resources.PontoResource import ponto_namespace
from flask_restplus import Api
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config/TestingConfig.py')
db = SQLAlchemy(app)
db.init_app(app)


SWAGGER_DOC = True

api = Api(app, title="Ponto Eletrônico API", doc="/" if SWAGGER_DOC is True else False, description="Api para consulta de Ponto Eletrônico")

def create_app():
    api.add_namespace(colaborador_namespace)
    api.add_namespace(ponto_namespace)
    return app
    