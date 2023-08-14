import pytest
from App_Code import create_app

app = create_app()


# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#
#     with app.test_client() as client:
#         yield client
#

@pytest.fixture
def authenticated_client(client):
    # Log in the test user.
    response = client.post('/login', data={'email': 'test@cgu.edu', 'password': 'hashed_password'})

    # Assert successful login, so if login fails, you'll know.
    assert response.status_code == 200 or response.status_code == 302
    return client


# Test cases for logout
def test_logout(client, authenticated_client, init_database):
    # # Test case 1: Successful logout
    response = authenticated_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

    # Test case 2: Logout when not logged in
    response_not_logged_in = authenticated_client.get('/logout', follow_redirects=True)
    assert response_not_logged_in.status_code == 200

    # Test case 3: Logout after login with a different user
    client.post('/login', data={'email': 'user2@cgu.edu', 'password': 'password'}, follow_redirects=True)
    response_wrong_user = authenticated_client.get('/logout', follow_redirects=True)
    assert response_wrong_user.status_code == 200
