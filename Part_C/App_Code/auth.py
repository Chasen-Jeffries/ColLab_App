from flask import Blueprint, render_template, redirect, url_for, request, flash 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

from flask_mail import Message
from . import mail
import jwt
from datetime import datetime, timedelta
from flask import current_app as app

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # IF a user does not provide a CGU email it will redirect back to signup page so user can try again
    allowed_domains = ['cgu.edu']
    domain = email.split('@')[1]
    if domain not in allowed_domains:
       flash('Please provide a CGU email address')
       return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/reset-password')
def reset_password():
    return render_template('reset_password.html')

@auth.route('/reset-password', methods=['POST'])
def send_password_reset_email():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        token = generate_password_reset_token(user)
        reset_url = url_for('auth.reset_with_token', token=token, _external=True)
        message = Message('Password Reset', sender='noreply@example.com', recipients=[email])
        message.body = f"Click the link to reset your password: {reset_url}"
        mail.send(message)
    flash('Password reset email sent. Please check your inbox.')
    return redirect(url_for('auth.login'))

@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    user = verify_password_reset_token(token)
    if not user:
        flash('Invalid or expired token.')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        # Process the password reset form
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password != confirm_password:
            flash('Passwords do not match.')
            return redirect(url_for('auth.reset_with_token', token=token))

        user.password = generate_password_hash(new_password, method='sha256')
        db.session.commit()

        flash('Your password has been reset successfully.')
        return redirect(url_for('auth.login'))

    return render_template('reset_password_with_token.html', token=token)

def generate_password_reset_token(user):
    token_data = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiry time (e.g., 1 hour)
    }
    token = jwt.encode(token_data, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@staticmethod
def verify_password_reset_token(token):
    try:
        token_data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = token_data.get('user_id')
        user = User.query.get(user_id)
        return user
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None
