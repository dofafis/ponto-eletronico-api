import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../app/')

import pytest
from app import create_app
from flask_restplus import Api
from multiprocessing import Process
from db import db
# Creates a fixture whose name is "app"
# and returns our flask server instance

print("Iniciando testes...")
@pytest.fixture(scope='session', autouse=True)
def client():
    app = create_app("TestingConfig")
    yield app.test_client()