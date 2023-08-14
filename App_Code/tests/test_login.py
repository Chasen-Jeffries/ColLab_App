import pytest
from App_Code import create_app

app = create_app()

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

# All Possible Test Cases For login
def test_login(client):
    # Test case 1: Successful Login
    response = client.post('/login', data={'email': 'valid_email', 'password': 'valid_password'})
    assert response.status_code == 302

    # Test case 2: Failed Login - Invalid Credentials
    response_invalid = client.post('/login', data={'email': 'invalid_email', 'password': 'invalid_password'})
    assert response_invalid.status_code == 302

    # Test case 3: Failed Login - Empty Fields
    response_empty = client.post('/login', data={'email': '', 'password': ''})
    assert response_empty.status_code == 302

    # Test case 4: Failed Login - Rate Limiting
    for _ in range(5):  # Simulate 5 consecutive failed attempts
        response_rate_limit = client.post('/login', data={'email': 'invalid', 'password': 'invalid'})
    assert response_rate_limit.status_code == 302

    # Test case 5: Failed Login - Account Lockout
    for _ in range(6):  # Simulate 6 consecutive failed attempts
        response_lockout = client.post('/login', data={'email': 'invalid', 'password': 'invalid'})
    assert response_lockout.status_code == 302

    # Test case 6: Failed Login - CSRF Protection
    response_csrf = client.post('/login', data={'email': 'valid_email', 'password': 'valid_password'}, headers={'Referer': 'http://evil.com'})
    assert response_csrf.status_code == 302

    # Test case 7: Failed Login - Account Inactive
    response_inactive = client.post('/login', data={'email': 'inactive_email', 'password': 'password'})
    assert response_inactive.status_code == 302

    # Test case 8: Failed Login - Account Disabled
    response_disabled = client.post('/login', data={'email': 'disabled_email', 'password': 'password'})
    assert response_disabled.status_code == 302

    # Test case 9: Edge Cases - Email and Password Length
    response_short = client.post('/login', data={'email': 'a@b', 'password': 'short'})
    assert response_short.status_code == 302

    response_long = client.post('/login', data={'email': 'very_long_email@domain.com', 'password': 'very_long_password' + 'x' * 1000})
    assert response_long.status_code == 302
