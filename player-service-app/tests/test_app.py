import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_players(client):
    response = client.get('/players')
    assert response.status_code == 200


def test_get_player_by_id(client):
    response = client.get('/players/1')
    assert response.status_code == 200
    assert response.json == {'id': 1, 'name': 'John Doe'}

def test_get_player_by_id_not_found(client):
    response = client.get('/players/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Player not found'}

def test_example(client):
    assert True
