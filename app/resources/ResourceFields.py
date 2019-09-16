from flask_restplus import Resource, Api, Namespace, fields

colaboradorPost = {
    'nome': fields.String(required=True, max_length=150, description='Nome do colaborador'),
    'cpf': fields.String(required=True, max_length=30, description='CPF do colaborador'),
    'email': fields.String(required=True, max_length=255, description='E-mail do colaborador'),
    'celular': fields.String(required=True, max_length=30, description='O número de celular do colaborador'),
    'empresa': fields.String(required=True, max_length=255, description='O nome da empresa associada ao colaborador'),
    'cargo': fields.String(required=True, max_length=255, description='O nome do cargo ocupado pelo colaborador'),
    'endereco': fields.String(required=True, max_length=150, description='O endereço com rua, número e bairro do colaborador'),
    'cep': fields.String(required=True, max_length=20, description='O número do CEP do colaborador'),
    'regras': fields.Integer(required=True)
}

colaboradorPut = {
    'nome': fields.String(max_length=150, description='Nome do colaborador'),
    'cpf': fields.String(max_length=30, description='CPF do colaborador'),
    'email': fields.String(max_length=255, description='E-mail do colaborador'),
    'celular': fields.String(max_length=30, description='O número de celular do colaborador'),
    'empresa': fields.String(max_length=255, description='O nome da empresa associada ao colaborador'),
    'cargo': fields.String(max_length=255, description='O nome do cargo ocupado pelo colaborador'),
    'endereco': fields.String(max_length=150, description='O endereço com rua, número e bairro do colaborador'),
    'cep': fields.String(max_length=20, description='O número do CEP do colaborador'),
    'regras': fields.Integer(),
    'ativo': fields.Boolean()
}

pontoPost = {
    'tipo_de_ponto': fields.String(required=True, max_length=10, description="Entrada ('in') ou Saída (out)"),
    'colaborador_id': fields.Integer(required=True)
}

pontoPut = {
    'tipo_de_ponto': fields.String(max_length=10, description="Entrada ('in') ou Saída (out)"),
    'colaborador_id': fields.Integer(),
    'created_at': fields.DateTime(),
    'last_modified_at': fields.DateTime()
}
