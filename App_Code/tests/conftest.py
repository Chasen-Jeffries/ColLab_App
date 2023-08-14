import pytest
from App_Code import create_app, db
from App_Code.models import User


@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    return app


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture
def init_database(app):
    with app.app_context():
        db.create_all()
        yield  # this ensures the setup runs before tests and the teardown runs after tests
        db.drop_all()


@pytest.fixture
def init_with_sample_user(init_database, app):
    with app.app_context():
        sample_user = User(email='test@cgu.edu', name='Test User', password='hashed_password')
        db.session.add(sample_user)
        db.session.commit()
        return sample_user


# Additional Test Cases for Configuration
def test_default_configuration(app):
    assert app.config['DEBUG'] is False  # Update with your default config value


def test_custom_configuration(app):
    app.config['DEBUG'] = True
    assert app.config['DEBUG'] is True


def test_configuration_override(app):
    app.config.from_object('config.testing')  # Assuming 'config.testing' holds custom config values
    assert app.config['DEBUG'] is True  # Verify that overridden value is used


def test_error_handling_missing_configuration(app):
    with pytest.raises(KeyError):
        missing_value = app.config['MISSING_CONFIG']  # Verify app handles missing config gracefully
