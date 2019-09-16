import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../app/')

import pytest
from run_tests import create_app
from flask_restplus import Api
from multiprocessing import Process

# Creates a fixture whose name is "app"
# and returns our flask server instance

app = create_app()
print("Pressione CTRL + C para verificar o resultado dos testes...")
print("Iniciando testes...")

@pytest.fixture(scope='session', autouse=True)
def client():
    yield app.test_client()