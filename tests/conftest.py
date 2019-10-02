import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../app/')

import pytest
from app import create_app
from flask_restplus import Api

print("Iniciando testes...")
@pytest.fixture(scope='session', autouse=True)
def client():
    app, db = create_app("TestingConfig")

    with app.app_context():
        db.create_all()
        yield app.test_client(), db
        db.drop_all()
    
    try:
        os.remove('tests/testing.db')
    except FileNotFoundError:
        pass
