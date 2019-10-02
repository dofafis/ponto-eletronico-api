import json
from models.Colaborador import Colaborador
from models.Ponto import Ponto

def test_post_ponto_in(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    
    db.session.add(colaborador)

    db.session.flush()
    db.session.commit()

    print('\n---------------------------------------------')
    print("Post Ponto iniciando...")

    url = '/ponto/'
    data = {
        "tipo_de_ponto": "in",
        "colaborador_id": colaborador.id
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = app.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    print("Post Colaborador antes do ponto finalizado...")
    print('---------------------------------------------')

def test_ponto_in_get(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    db.session.add(colaborador)
    db.session.flush()
    db.session.commit()

    ponto_in = Ponto(tipo_de_ponto="in", colaborador_id=colaborador.id)
    db.session.add(ponto_in)
    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Get Ponto In iniciando...")
    response = app.get('/ponto/' + str(ponto_in.id))
    print("Response: ", response.json)
    assert response.status_code == 200
    print('Get Ponto In finalizado...')
    print('---------------------------------------------')

def test_post_ponto_out(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    db.session.add(colaborador)
    db.session.flush()
    db.session.commit()
    
    print('\n---------------------------------------------')
    print("Post Ponto iniciando...")

    url = '/ponto/'
    data = {
        "tipo_de_ponto": "out",
        "colaborador_id": colaborador.id
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = app.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200

    print("Post Colaborador antes do ponto finalizado...")
    print('---------------------------------------------')

def test_ponto_out_get(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    db.session.add(colaborador)
    db.session.flush()
    db.session.commit()

    ponto_out = Ponto(tipo_de_ponto="out", colaborador_id=colaborador.id)
    db.session.add(ponto_out)
    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Get Ponto Out iniciando...")
    response = app.get('/ponto/' + str(ponto_out.id))
    print("Response: ", response.json)
    assert response.status_code == 200
    print('Get Ponto Out finalizado...')
    print('---------------------------------------------')

def test_ponto_out_put(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    db.session.add(colaborador)
    db.session.flush()
    db.session.commit()

    ponto_out = Ponto(tipo_de_ponto="out", colaborador_id=colaborador.id)
    db.session.add(ponto_out)
    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Put Ponto Out iniciando...")

    url = '/ponto/' + str(ponto_out.id)
    data = {
        "created_at": "2019-09-16T20:38:43.563Z",
        "last_modified_at": "2019-09-16T20:38:43.563Z"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = app.put(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    print("Put Ponto Out finalizado...")
    print('---------------------------------------------')

def test_ponto_in_delete(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    db.session.add(colaborador)
    db.session.flush()
    db.session.commit()

    ponto_in = Ponto(tipo_de_ponto="in", colaborador_id=colaborador.id)
    db.session.add(ponto_in)
    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Delete Ponto In iniciando...")
    response = app.delete('/ponto/' + str(ponto_in.id))
    assert response.status_code == 200
    print("Delete Ponto In finalizado...")
    print('---------------------------------------------')

def test_ponto_out_delete(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    db.session.add(colaborador)
    db.session.flush()
    db.session.commit()

    ponto_out = Ponto(tipo_de_ponto="out", colaborador_id=colaborador.id)
    db.session.add(ponto_out)
    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Delete Ponto Out iniciando...")
    response = app.delete('/ponto/' + str(ponto_out.id))
    assert response.status_code == 200
    print("Delete Ponto Out finalizado...")
    print('---------------------------------------------')
