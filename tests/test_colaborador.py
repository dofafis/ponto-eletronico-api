import json
from models.Colaborador import Colaborador

def test_post_colaborador(client):
    app,db = client[0],client[1]
    print('\n---------------------------------------------')
    print("Post Colaborador iniciando...")

    url = '/colaborador/'
    data = {
        "nome": "Lucas Farias de Oliveira",
        "cpf": "02142020210",
        "email": "lfo@icomp.ufam.edu.br",
        "celular": "92999999999",
        "empresa": "Pontotel",
        "cargo": "Desenvolvedor Jr",
        "endereco": "Rua 123, n 123, bairro ABCDE",
        "cep": "69099999",
        "regras": 0
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = app.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200

    print("Post Colaborador finalizado...")
    print('---------------------------------------------')


def test_colaborador_get(client):
    app,db = client[0],client[1]

    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)

    db.session.add(colaborador)

    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Get Colaborador iniciando...")
    response = app.get('/colaborador/' + str(colaborador.id))
    print("Response: ", response.json)
    assert response.status_code == 200
    print('Get Colaborador finalizado...')
    print('---------------------------------------------')


def test_post_colaborador_repetido(client):    
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)

    db.session.add(colaborador)

    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Post Colaborador repetido iniciando...")

    url = '/colaborador/'
    data = {
        "nome": "Lucas Farias de Oliveira",
        "cpf": "02142020210",
        "email": "lfo@icomp.ufam.edu.br",
        "celular": "92999999999",
        "empresa": "Pontotel",
        "cargo": "Desenvolvedor Jr",
        "endereco": "Rua 123, n 123, bairro ABCDE",
        "cep": "69099999",
        "regras": 0
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = app.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    print("Post Colaborador repetido finalizado...")
    print('---------------------------------------------')


def test_colaborador_put(client):
    app, db = client[0], client[1]
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    
    db.session.add(colaborador)

    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Put Colaborador iniciando...")

    url = '/colaborador/' + str(colaborador.id)
    data = {
        "nome": "João Farias de Oliveira",
        "cpf": "02142020211"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = app.put(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    print("Put Colaborador finalizado...")
    print('---------------------------------------------')

def test_colaborador_delete(client):
    app, db = client[0], client[1]

    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    
    db.session.add(colaborador)

    db.session.flush()
    db.session.commit()

    global id
    print('---------------------------------------------')
    print("Delete Colaborador iniciando...")
    response = app.delete('/colaborador/' + str(colaborador.id))
    assert response.status_code == 200
    print("Delete Colaborador finalizado...")
    print('---------------------------------------------')

def test_colaborador_hard_delete(client):
    app, db = client[0], client[1]
    
    colaborador = Colaborador(nome="Lucas Farias de Oliveira",cpf="02142020210",email="lfo@icomp.ufam.edu.br",celular="92999999999",empresa="Pontotel",cargo="Desenvolvedor Jr",endereco="Rua 123, n 123, bairro ABCDE",cep="69099999",ativo=True)
    
    db.session.add(colaborador)

    db.session.flush()
    db.session.commit()

    print('---------------------------------------------')
    print("Hard Delete Colaborador iniciando...")
    response = app.delete('/colaborador/hard_delete/' + str(colaborador.id))
    assert response.status_code == 200
    print("Hard Delete Colaborador finalizado...")
    print('---------------------------------------------')
