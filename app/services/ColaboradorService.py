from app import db
from models.Colaborador import Colaborador

class ColaboradorService():
    def colaboradorToJson(self, colaborador):
        json = {
            'id': colaborador.id,
            'nome': colaborador.nome,
            'cpf': colaborador.cpf,
            'email': colaborador.email,
            'celular': colaborador.celular,
            'empresa': colaborador.empresa,
            'cargo': colaborador.cargo,
            'endereco': colaborador.endereco,
            'cep': colaborador.cep,
            'ativo': colaborador.ativo,
            'created_at': str(colaborador.created_at),
            'last_modified_at': str(colaborador.last_modified_at)
        }
        return json

    def getAll(self):
        colaboradores = Colaborador.query.filter_by()
        colaboradores = list(self.colaboradorToJson(colaborador) for colaborador in colaboradores)
        return {'status': 'success', 'message': 'A lista de colaboradores foi consultada com sucesso', 'colaboradores': colaboradores}

    def getByCpf(self, cpf):
        colaboradores = Colaborador.query.filter_by(cpf=cpf)
        colaboradores = list(self.colaboradorToJson(colaborador) for colaborador in colaboradores)
        return {'status': 'success', 'message': 'A lista de colaboradores foi consultada com sucesso', 'colaboradores': colaboradores}

    def getById(self, id):
        if not id:
            return {'status': 'fail', 'message': 'O parâmetro id é obrigatório'}, 400
        else:
            try:
                colaborador = Colaborador.query.filter_by(id=id, ativo=True).first()
                if colaborador:
                    response_object = { 'status': 'success', 'message': 'Consulta realizada com sucesso', 'colaborador': self.colaboradorToJson(colaborador)}
                    return response_object, 200
                else:
                    return  {'status': 'fail', 'message': 'Não existe colaborador ativo associado a este id'}, 400
            except Exception as err:
                return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
            finally:
                db.session.close()

    def save(self, data):
        colaborador = Colaborador.query.filter_by(cpf=data['cpf'], ativo=True).first()

        if not colaborador:
            colaborador = Colaborador(
                nome=data['nome'],
                cpf=data['cpf'],
                email=data['email'],
                celular=data['celular'],
                empresa=data['empresa'],
                cargo=data['cargo'],
                endereco=data['endereco'],
                cep=data['cep'],
                ativo=True
            )

            db.session.add(colaborador)
            try:
                db.session.flush()
                db.session.commit()
                return {'status': 'success', 'message': 'Colaborador adicionado com sucesso', 'id': colaborador.id}, 200
            except Exception as err:
                db.session.rollback()
                return {'status': 'fail', 'message': 'Não foi possível adicionar o colaborador no momento'}, 500
            finally:
                db.session.close()

        else:
            return {'status': 'fail', 'message': 'Já existe um colaborador ativo com este CPF'}, 400

    def update(self, id, data):
        if not id:
            return {'status': 'fail', 'message': 'O parâmetro id é obrigatório'}, 400
        else:
            try:
                colaborador = Colaborador.query.filter_by(id=id, ativo=True).first()

                if not colaborador:
                    return {'status': 'fail', 'message': 'Não existe colaborador associado ao id recebido'}, 400
                else:
                    colaborador.nome = data['nome'] if 'nome' in data else colaborador.nome
                    colaborador.cpf = data['cpf'] if 'cpf' in data else colaborador.cpf
                    colaborador.email = data['email'] if 'email' in data else colaborador.email
                    colaborador.celular = data['celular'] if 'celular' in data else colaborador.celular
                    colaborador.empresa = data['empresa'] if 'empresa' in data else colaborador.empresa
                    colaborador.cargo = data['cargo'] if 'cargo' in data else colaborador.cargo
                    colaborador.endereco = data['endereco'] if 'endereco' in data else colaborador.endereco
                    colaborador.cep = data['cep'] if 'cep' in data else colaborador.cep
                    colaborador.ativo = data['ativo'] if 'ativo' in data else colaborador.ativo

                    try:
                        db.session.commit()
                        return {'status': 'success', 'message': 'Colaborador atualizado com sucesso'}, 200
                    except Exception as err:
                        db.session.rollback()
                        return {'status': 'fail', 'message': 'Não foi possível atualizar o colaborador no momento'}, 500
                    finally:
                        db.session.close()
            except Exception as err:
                return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
            finally:
                db.session.close()

    def delete(self, id):
        if not id:
            return {'status': 'fail', 'message': 'O parâmetro id é obrigatório'}, 400
        else:
            try:
                colaborador = Colaborador.query.filter_by(id=id, ativo=True).first()

                if not colaborador:
                    return {'status': 'fail', 'message': 'Não existe usuário associado ao id recebido'}, 400
                else:
                    colaborador.ativo = False
                    try:
                        db.session.commit()
                        return {'status': 'success', 'message': 'O colaborador foi removido com sucesso.'}, 200
                    except Exception as err:
                        return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
                    finally:
                        db.session.close()
            except Exception as err:
                return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
            finally:
                db.session.close()
    
    def hard_delete(self, id):
        if not id:
            return {'status': 'fail', 'message': 'O parâmetro id é obrigatório'}, 400
        else:
            try:
                colaborador = Colaborador.query.filter_by(id=id).first()

                if not colaborador:
                    return {'status': 'fail', 'message': 'Não existe usuário associado ao id recebido'}, 400
                else:
                    db.session.delete(colaborador)
                    try:
                        db.session.commit()
                        return {'status': 'success', 'message': 'O colaborador foi removido permanente com sucesso.'}, 200
                    except Exception as err:
                        return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
                    finally:
                        db.session.close()
            except Exception as err:
                return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
            finally:
                db.session.close()
    