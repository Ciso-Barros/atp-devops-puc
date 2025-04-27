import pytest
from app.app import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True  
    with app.test_client() as client:
        yield client

# [Mantenha os mesmos 5 testes que você tinha antes]
def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Funcionando no Docker!" in response.data

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

# Teste 3: Verifica o tratamento de erro 404
def test_not_found_error(client):
    response = client.get('/rota_inexistente')
    assert response.status_code == 404
    assert response.json == {"error": "Endpoint not found"}

# Teste 4: Verifica o Content-Type da rota principal
def test_hello_content_type(client):
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

# Teste 5: Verifica o Content-Type da rota health
def test_health_content_type(client):
    response = client.get('/health')
    assert response.content_type == 'application/json'