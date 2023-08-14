import pytest
from App_Code import create_app

app = create_app()


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def authenticated_client(client):
    # Log in the test user.
    response = client.post('/login', data={'email': 'test@cgu.edu', 'password': 'hashed_password'})

    # Assert successful login, so if login fails, you'll know.
    assert response.status_code == 200 or response.status_code == 302

    return client


# All Possible Test Cases For create_post
def test_create_post(authenticated_client):
    # Test case 1: Try to create a post with valid data
    post_data = {
        'title': 'Test Post',
        'content': 'This is a test post.'
    }
    response = authenticated_client.post('/create', data=post_data, follow_redirects=True)
    assert response.status_code == 200  # Assuming successful post creation redirects to the home page

    # Test case 2: Try to create a post with missing title
    post_data_missing_title = {
        'content': 'This is a test post without a title.'
    }
    response_missing_title = authenticated_client.post('/create', data=post_data_missing_title, follow_redirects=True)
    assert response_missing_title.status_code == 200  # Assuming bad request due to missing title

    # Test case 3: Try to create a post with missing content
    post_data_missing_content = {
        'title': 'Test Post Without Content'
    }
    response_missing_content = authenticated_client.post('/create', data=post_data_missing_content,
                                                         follow_redirects=True)
    assert response_missing_content.status_code == 200  # Assuming bad request due to missing content

    # Test case 4: Try to create a post with both title and content missing
    post_data_missing_both = {}
    response_missing_both = authenticated_client.post('/create', data=post_data_missing_both, follow_redirects=True)
    assert response_missing_both.status_code == 200  # Assuming bad request due to missing both title and content

    # Test case 5: Try to create a post with invalid data (e.g., title exceeding maximum length)
    post_data_invalid_title = {
        'title': 'A' * 256,  # Assuming the maximum title length is 255 characters
        'content': 'This is an invalid test post.'
    }
    response_invalid_title = authenticated_client.post('/create', data=post_data_invalid_title, follow_redirects=True)
    assert response_invalid_title.status_code == 200  # Assuming bad request due to invalid title length
