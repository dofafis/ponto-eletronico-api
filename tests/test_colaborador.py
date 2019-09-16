import json

id = 0
def test_post_colaborador(client):
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

    response = client.post(url, data=json.dumps(data), headers=headers)
    global id
    assert response.status_code == 200
    #if successful
    id = response.json['id']
    print("Post Colaborador finalizado...")
    print('---------------------------------------------')

def test_colaborador_get(client):
    global id
    print('---------------------------------------------')
    print("Get Colaborador iniciando...")
    response = client.get('/colaborador/' + str(id))
    print("Response: ", response.json)
    assert response.status_code == 200
    print('Get Colaborador finalizado...')
    print('---------------------------------------------')

def test_post_colaborador_repetido(client):
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

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
    print("Post Colaborador repetido finalizado...")
    print('---------------------------------------------')

def test_colaborador_put(client):
    print('---------------------------------------------')
    print("Put Colaborador iniciando...")
    global id
    url = '/colaborador/' + str(id)
    data = {
        "nome": "João Farias de Oliveira",
        "cpf": "02142020211"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.put(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    print("Put Colaborador finalizado...")
    print('---------------------------------------------')

def test_colaborador_delete(client):
    global id
    print('---------------------------------------------')
    print("Delete Colaborador iniciando...")
    response = client.delete('/colaborador/' + str(id))
    assert response.status_code == 200
    print("Delete Colaborador finalizado...")
    print('---------------------------------------------')

def test_colaborador_hard_delete(client):
    global id
    print('---------------------------------------------')
    print("Hard Delete Colaborador iniciando...")
    response = client.delete('/colaborador/hard_delete/' + str(id))
    assert response.status_code == 200
    print("Hard Delete Colaborador finalizado...")
    print('---------------------------------------------')