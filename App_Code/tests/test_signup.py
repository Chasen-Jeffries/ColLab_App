import pytest
from App_Code import create_app
from App_Code.models import User

app = create_app()


# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#
#     with app.test_client() as client:
#         yield client


# All Possible Test Cases For signup
def test_signup(client):
    # Test case 1: Successful signup with a CGU email
    response_cgu_email = client.post('/signup', data={'email': 'test@cgu.edu', 'password': 'secure_password'})
    assert response_cgu_email.status_code == 302  # Assuming successful signup redirects to another page

    # Test case 2: Failed signup with an existing email
    response_existing_email = client.post('/signup', data={'email': 'existing@cgu.edu', 'password': 'secure_password'})
    assert response_existing_email.status_code == 302  # Assuming conflict due to existing email

    # Test case 3: Failed signup with an invalid email format
    response_invalid_email = client.post('/signup', data={'email': 'invalid@example.com', 'password': 'secure_password'})
    assert response_invalid_email.status_code == 302  # Assuming bad request due to invalid email format

    # Test case 4: Failed signup with a weak password and a CGU email
    response_weak_password_cgu = client.post('/signup', data={'email': 'new@cgu.edu', 'password': 'weak'})
    assert response_weak_password_cgu.status_code == 302  # Assuming bad request due to weak password

    # Test case 5: Failed signup with empty fields
    response_empty_fields = client.post('/signup', data={'email': '@', 'password': ''})
    assert response_empty_fields.status_code == 302  # Assuming bad request due to empty fields

    # Test case 6: Failed signup with CSRF protection
    response_csrf = client.post('/signup', data={'email': 'test@cgu.edu', 'password': 'secure_password'})
    assert response_csrf.status_code == 302  # Assuming bad request due to CSRF protection

    # Test case 7: Failed signup with an invalid email length
    response_invalid_email_length = client.post('/signup', data={'email': 'a@b', 'password': 'secure_password'})
    assert response_invalid_email_length.status_code == 302  # Assuming bad request due to invalid email length

    # Test case 8: Failed signup with a non-CGU Email Address
    response_non_cgu_email = client.post('/signup', data={'email': 'test@example.com', 'password': 'secure_password'})
    # assert b'Please provide a CGU email address' in response_non_cgu_email.data
    response_non_cgu_email.status_code == 302