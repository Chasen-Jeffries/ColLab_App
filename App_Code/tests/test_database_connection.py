import pytest
from App_Code import create_app, db

app = create_app()


@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# Test case for database connection
def test_database_connection():
    with app.app_context():
        try:
            db.engine.connect()
            assert True  # Successfully connected to the database
        except Exception as e:
            assert False, f"Database connection test failed: {e}"
