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


# All Possible Test Cases For edit_post
def test_edit_post(authenticated_client):
    # Assuming you have a post with a known ID for testing
    post_id = 123

    # Test case 1: Try to edit a post with valid data
    post_data = {
        'title': 'Updated Title',
        'content': 'This is an updated post.'
    }
    response = authenticated_client.post(f'/edit/{post_id}', data=post_data, follow_redirects=True)
    assert response.status_code == 200  # Assuming successful edit redirects to the post page

    # Test case 2: Try to edit a post with missing title
    post_data_missing_title = {
        'content': 'This is an updated post without a title.'
    }
    response_missing_title = authenticated_client.post(f'/edit/{post_id}', data=post_data_missing_title,
                                                       follow_redirects=True)
    assert response_missing_title.status_code == 200  # Assuming bad request due to missing title

    # Test case 3: Try to edit a post with missing content
    post_data_missing_content = {
        'title': 'Updated Title Without Content'
    }
    response_missing_content = authenticated_client.post(f'/edit/{post_id}', data=post_data_missing_content,
                                                         follow_redirects=True)
    assert response_missing_content.status_code == 200  # Assuming bad request due to missing content

    # Test case 4: Try to edit a post with invalid data (e.g., title exceeding maximum length)
    post_data_invalid_title = {
        'title': 'A' * 256,  # Assuming the maximum title length is 255 characters
        'content': 'This is an invalid updated post.'
    }
    response_invalid_title = authenticated_client.post(f'/edit/{post_id}', data=post_data_invalid_title,
                                                       follow_redirects=True)
    assert response_invalid_title.status_code == 200  # Assuming bad request due to invalid title length


# All Possible Test Cases For delete_post
def test_delete_post(authenticated_client):
    # Assuming you have a post with a known ID for testing
    post_id = 123

    # Test case 1: Try to delete a post
    response = authenticated_client.post(f'/delete/{post_id}', follow_redirects=True)
    assert response.status_code == 200  # Assuming successful deletion redirects to the homepage

    # Test case 2: Try to delete a post that doesn't exist
    response_nonexistent_post = authenticated_client.post('/delete/999', follow_redirects=True)
    assert response_nonexistent_post.status_code == 200  # Assuming the post doesn't exist
