from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from .main import main as main_blueprint

# Initialize SQLAlchemy, Mail, and other extensions
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Flask-Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
    app.config['MAIL_PASSWORD'] = 'your-password'
    app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

    db.init_app(app)
    mail.init_app(app)

    # Import blueprints
    from .main import main as main_blueprint
    from .research import research as research_blueprint


    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(research_blueprint, url_prefix='/research')

    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app

