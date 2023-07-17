import pytest
from App_Code import create_app

app = create_app()

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login(client):
    response = client.post('/login', data={'email': 'valid_email', 'password': 'valid_password'})
    assert response.status_code == 302


def test_create_post(client):
    # Try to create a post
    post_data = {
        'title': 'Test Post',
        'content': 'This is a test post.'
    }
    response = client.post('/create', data=post_data, follow_redirects=True)

    # Assuming that a successful post creation will redirect to the home page
    assert response.status_code == 200







