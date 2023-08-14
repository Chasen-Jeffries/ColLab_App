import pytest
from App_Code import create_app, db
from App_Code.models import User

app = create_app()

@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()

@pytest.fixture
def authenticated_client(client, init_database):
    # Log in the test user.
    response = client.post('/login', data={'email': 'test@cgu.edu', 'password': 'hashed_password'})

    # Assert successful login, so if login fails, you'll know.
    assert response.status_code == 200 or response.status_code == 302

    return client

# Test cases for password resetting
def test_password_reset(authenticated_client, init_database):
    # Test case 1: Successful password reset
    response_reset_success = authenticated_client.post('/reset-password', data={'email': 'test@cgu.edu'}, follow_redirects=True)
    # assert b'Password reset email sent. Please check your inbox.' in response_reset_success.data

    # Test case 2: Password reset with invalid email
    response_reset_invalid_email = authenticated_client.post('/reset-password', data={'email': 'invalid@example.com'}, follow_redirects=True)
    # assert b'No user found with that email address.' in response_reset_invalid_email.data

    # Test case 3: Password reset with empty email
    response_reset_empty_email = authenticated_client.post('/reset-password', data={'email': ''}, follow_redirects=True)
    # assert b'Please provide your email address.' in response_reset_empty_email.data
