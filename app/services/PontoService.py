from app import db
from sqlalchemy import extract
from datetime import datetime
from models.Ponto import Ponto
from collections import defaultdict

class PontoService():
    def pontoToJson(self, ponto):
        json = {
            'id': ponto.id,
            'tipo_de_ponto': ponto.tipo_de_ponto,
            'created_at': str(ponto.created_at),
            'last_modified_at': str(ponto.last_modified_at)
        }
        return json

    def getAll(self):
        pontos = ponto.query.filter_by()
        pontos = list(self.colaboradorToJson(ponto) for ponto in pontos);
        return {'status': 'success', 'message': 'A lista de pontos foi consultada com sucesso', 'pontos': pontos}

    def report(self, colaborador_id, month):
        if colaborador_id and month:
            pontos = self.getByColaboradorIdAndMonth(colaborador_id, month)

            if not pontos:
                return {'status': 'fail', 'message': 'Não há pontos registrados para este colaborador este mês'}, 200
            aux = []
            days = defaultdict(list)
            for ponto in pontos:
                day = ponto.created_at.day
                days[day].append(ponto)

            report = []
            for day in days:
                ins = list(filter(lambda ponto: ponto.tipo_de_ponto=='in', days[day]))
                outs = list(filter(lambda ponto: ponto.tipo_de_ponto=='out', days[day]))
                days[day] = 0
                if len(ins) > 0 and len(outs) > 0:
                    if ins[0].created_at < outs[-1].created_at:
                        days[day] = float(str(abs(outs[-1].created_at - ins[0].created_at).total_seconds())) / float(3600)
                report.append({
                    "day": day,
                    "work_hours": round(days[day], 5)
                })
            return {'status': 'success', 'message': 'Relatório de ponto consultado com sucesso.', 'report': report}, 200
        else:
            return {'status': 'fail', 'message': 'Os campos colaborador_id e month são obrigatórios'}

    def getByColaboradorIdAndMonth(self, colaborador_id, month):
        if colaborador_id and month:
            pontos = Ponto.query.filter(Ponto.colaborador_id==colaborador_id, extract('month', Ponto.created_at)==month).order_by(Ponto.created_at).all()
        elif colaborador_id:
            pontos = Ponto.query.filter_by(colaborador_id=colaborador_id).order_by(Ponto.created_at)
        elif month:
            pontos = Ponto.query.filter(extract('month', Ponto.created_at)==month).order_by(Ponto.created_at).all()
        else:
            pontos = Ponto.query.filter_by().order_by(Ponto.created_at)

        #pontos = list(self.pontoToJson(ponto) for ponto in pontos)
        return pontos

    def getById(self, id):
        if not id:
            return {'status': 'fail', 'message': 'O parâmetro id é obrigatório'}, 400
        else:
            try:
                ponto = Ponto.query.filter_by(id=id).first()
                print(ponto)
                if ponto:
                    response_object = { 'status': 'success', 'message': 'Consulta realizada com sucesso', 'ponto': self.pontoToJson(ponto)}
                    return response_object, 200
                else:
                    return  {'status': 'fail', 'message': 'Não existe ponto associado a este id'}, 400
            except Exception as err:
                return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.', 'err': err}, 500
            finally:
                db.session.close()

    def save(self, data):
        ponto = Ponto(
            tipo_de_ponto=data['tipo_de_ponto'],
            colaborador_id=data['colaborador_id']
        )

        db.session.add(ponto)
        try:
            db.session.flush()
            db.session.commit()
            return {'status': 'success', 'message': 'Ponto adicionado com sucesso', 'id': ponto.id}, 200
        except Exception as err:
            db.session.rollback()
            return {'status': 'fail', 'message': 'Não foi possível adicionar o ponto no momento'}, 500
        finally:
            db.session.close()

    def update(self, id, data):
        if not id:
            return {'status': 'fail', 'message': 'O parâmetro id é obrigatório'}, 400
        else:
            try:
                ponto = Ponto.query.filter_by(id=id).first()

                if not ponto:
                    return {'status': 'fail', 'message': 'Não existe ponto associado ao id recebido'}, 400
                else:
                    ponto.tipo_de_ponto = data['tipo_de_ponto'] if 'tipo_de_ponto' in data else ponto.tipo_de_ponto
                    ponto.colaborador_id = data['colaborador_id'] if 'colaborador_id' in data else ponto.colaborador_id
                    ponto.created_at = data['created_at'] if 'created_at' in data else ponto.created_at
                    ponto.last_modified_at = data['last_modified_at'] if 'last_modified_at' in data else ponto.last_modified_at

                    try:
                        db.session.commit()
                        return {'status': 'success', 'message': 'Ponto atualizado com sucesso'}, 200
                    except Exception as err:
                        db.session.rollback()
                        return {'status': 'fail', 'message': 'Não foi possível atualizar o ponto no momento'}, 500
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
                ponto = Ponto.query.filter_by().first()

                if not ponto:
                    return {'status': 'fail', 'message': 'Não existe ponto associado ao id recebido'}, 400
                else:
                    db.session.delete(ponto)
                    try:
                        db.session.commit()
                        return {'status': 'success', 'message': 'O ponto foi removido com sucesso.'}, 200
                    except Exception as err:
                        return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
                    finally:
                        db.session.close()
            except Exception as err:
                return {'status': 'fail', 'message': 'Não foi possível completar a solicitação no momento, por favor tente novamente mais tarde.'}, 500
            finally:
                db.session.close()
    