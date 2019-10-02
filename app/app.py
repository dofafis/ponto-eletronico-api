from flask import Flask, request
from resources.ColaboradorResource import colaborador_namespace
from resources.PontoResource import ponto_namespace
from flask_restplus import Api
SWAGGER_DOC = True

def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile('../config/' + config + '.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app, title="Ponto Eletrônico API", doc="/" if SWAGGER_DOC is True else False, description="Api para consulta de Ponto Eletrônico")

    api.add_namespace(colaborador_namespace)
    api.add_namespace(ponto_namespace)
    from db import db
    db.init_app(app)
    return app, db