from flask import Flask, request
from flask_restplus import Resource, Api, Namespace, fields
from services.ColaboradorService import ColaboradorService
from .ResourceFields import colaboradorPost, colaboradorPut

colaborador_namespace = Namespace("Colaborador", path="/colaborador", description="Api com as operações relacionadas a colaborador(es)")

colaborador_service = ColaboradorService()

colaboradorPostFields = colaborador_namespace.model('Colaborador', colaboradorPost)
colaboradorPutFields = colaborador_namespace.model('Colaborador', colaboradorPut)

@colaborador_namespace.route('/')
class CreateAndReadOptions(Resource):

    @colaborador_namespace.expect(colaboradorPostFields)
    def post(self):
        print(request.json)
        return colaborador_service.save(request.json)

    @colaborador_namespace.param('cpf', 'Parâmetro opcional, caso queira a lista de colaboradores ativos e inativos com um cpf')
    def get(self):
        if 'cpf' in request.args:
            return colaborador_service.getByCpf(request.args['cpf'])
        return colaborador_service.getAll()

@colaborador_namespace.route('/<int:id>')
class ReadUpdateAndDelete(Resource):
    def get(self, id):
        return colaborador_service.getById(id)

    @colaborador_namespace.expect(colaboradorPutFields)
    def put(self, id):
        return colaborador_service.update(id, request.json)

    def delete(self, id):
        return colaborador_service.delete(id)

@colaborador_namespace.route('/hard_delete/<int:id>')
class HardDelete(Resource):
    def delete(self, id):
        return colaborador_service.hard_delete(id)

colaborador_namespace.add_resource(CreateAndReadOptions)
colaborador_namespace.add_resource(ReadUpdateAndDelete)
colaborador_namespace.add_resource(HardDelete)
