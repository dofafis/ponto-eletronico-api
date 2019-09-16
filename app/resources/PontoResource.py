from flask import Flask, request
from flask_restplus import Resource, Api, Namespace, fields
from services.PontoService import PontoService
from .ResourceFields import pontoPost, pontoPut

ponto_namespace = Namespace("Ponto", path="/ponto", description="Api com as operações relacionadas a ponto(es)")

ponto_service = PontoService()

pontoPostFields = ponto_namespace.model('PontoPost', pontoPost)
pontoPutFields = ponto_namespace.model('PontoPost', pontoPut)

@ponto_namespace.route('/')
class Create(Resource):

    @ponto_namespace.expect(pontoPostFields)
    def post(self):
        print(request.json)
        return ponto_service.save(request.json)

@ponto_namespace.route('/<int:id>')
class ReadUpdateAndDelete(Resource):
    def get(self, id):
        return ponto_service.getById(id)

    @ponto_namespace.expect(pontoPutFields)
    def put(self, id):
        return ponto_service.update(id, request.json)

    def delete(self, id):
        return ponto_service.delete(id)

@ponto_namespace.route('/report/<int:colaborador_id>/<int:month>')
class ReadOptions(Resource):
    def get(self, colaborador_id, month):
        return ponto_service.report(colaborador_id, month)

ponto_namespace.add_resource(Create)
ponto_namespace.add_resource(ReadUpdateAndDelete)
ponto_namespace.add_resource(ReadOptions)
