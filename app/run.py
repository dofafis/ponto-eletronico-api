from app import app
from resources.ColaboradorResource import colaborador_namespace
from resources.PontoResource import ponto_namespace
from flask_restplus import Api
SWAGGER_DOC = True
api = Api(app, title="Ponto Eletrônico API", doc="/" if SWAGGER_DOC is True else False, description="Api para consulta de Ponto Eletrônico")

def create_app():
    api.add_namespace(colaborador_namespace)
    api.add_namespace(ponto_namespace)
    
    app.run()
    return app

create_app()