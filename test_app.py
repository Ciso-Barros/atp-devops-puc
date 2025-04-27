import pytest
from app.app import app  # Ajuste conforme sua estrutura

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    """Testa se a rota principal retorna a mensagem esperada"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"API DevOps PUC - Funcionando no Docker!" in response.data

def test_health_route(client):
    """Testa se a rota health retorna status healthy"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_404_error(client):
    """Testa se rotas inexistentes retornam 404"""
    response = client.get('/rota_inexistente')
    assert response.status_code == 404
    assert response.json == {"error": "Endpoint not found"}

def test_hello_route_content_type(client):
    """Testa se o content-type da rota principal é text/html"""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

def test_health_route_content_type(client):
    """Testa se o content-type da rota health é application/json"""
    response = client.get('/health')
    assert response.content_type == 'application/json'