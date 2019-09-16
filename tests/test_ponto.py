import json

id = 0
id_ponto_in = 0
id_ponto_out = 0

def test_post_colaborador_before_ponto(client):
    print('\n---------------------------------------------')
    print("Preparando para testar ponto...")

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
    print("Preparação para testar ponto finalizada...")
    print('---------------------------------------------')

def test_post_ponto_in(client):
    print('\n---------------------------------------------')
    print("Post Ponto iniciando...")

    global id
    global id_ponto_in
    url = '/ponto/'
    data = {
        "tipo_de_ponto": "in",
        "colaborador_id": id
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    #if successful
    id_ponto_in = response.json['id']
    print("Post Colaborador antes do ponto finalizado...")
    print('---------------------------------------------')

def test_ponto_in_get(client):
    global id_ponto_in
    print('---------------------------------------------')
    print("Get Ponto In iniciando...")
    response = client.get('/ponto/' + str(id_ponto_in))
    print("Response: ", response.json)
    assert response.status_code == 200
    print('Get Ponto In finalizado...')
    print('---------------------------------------------')

def test_post_ponto_out(client):
    print('\n---------------------------------------------')
    print("Post Ponto iniciando...")

    global id
    global id_ponto_out
    url = '/ponto/'
    data = {
        "tipo_de_ponto": "out",
        "colaborador_id": id
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    #if successful
    id_ponto_out = response.json['id']
    print("Post Colaborador antes do ponto finalizado...")
    print('---------------------------------------------')

def test_ponto_out_get(client):
    global id_ponto_out
    print('---------------------------------------------')
    print("Get Ponto Out iniciando...")
    response = client.get('/ponto/' + str(id_ponto_out))
    print("Response: ", response.json)
    assert response.status_code == 200
    print('Get Ponto Out finalizado...')
    print('---------------------------------------------')

def test_ponto_out_put(client):
    print('---------------------------------------------')
    print("Put Ponto Out iniciando...")
    global id_ponto_out
    url = '/ponto/' + str(id_ponto_out)
    data = {
        "created_at": "2019-09-16T20:38:43.563Z",
        "last_modified_at": "2019-09-16T20:38:43.563Z"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.put(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    print("Put Ponto Out finalizado...")
    print('---------------------------------------------')

def test_ponto_in_delete(client):
    global id
    print('---------------------------------------------')
    print("Delete Ponto In iniciando...")
    response = client.delete('/ponto/' + str(id_ponto_in))
    assert response.status_code == 200
    print("Delete Ponto In finalizado...")
    print('---------------------------------------------')

def test_ponto_out_delete(client):
    global id
    print('---------------------------------------------')
    print("Delete Ponto Out iniciando...")
    response = client.delete('/ponto/' + str(id_ponto_out))
    assert response.status_code == 200
    print("Delete Ponto Out finalizado...")
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
    response = client.delete('/colaborador/hard_delete/' + str(id))
    assert response.status_code == 200