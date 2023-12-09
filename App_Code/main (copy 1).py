from flask import Flask, Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
import sqlite3
from datetime import datetime

# Create a Blueprint for the main part of the application
main = Blueprint('main', __name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to get a specific post
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# Function to get all posts
def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts

# Index route
@main.route('/')
def index():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)

# Profile route
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# Individual post route
@main.route('/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# Create post route
@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    # ... existing create post logic ...
    return render_template('create.html')

# Edit post route
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    # ... existing edit post logic ...
    return render_template('edit.html', post=post)

# Delete post route
@main.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    # ... existing delete post logic ...
    return redirect(url_for('main.index'))

# About page route
@main.route('/about')
def about():
    return render_template('about.html')

# Research page route
@main.route('/research')
def research():
    posts = get_all_posts()
    return render_template('research.html', posts=posts)

# Search page route
@main.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

# Search results route
@main.route('/search-results', methods=['GET'])
def search_results():
    # ... existing search results logic ...
    return render_template('search_results.html', query=query, matching_posts=matching_posts)

# Routes for Norse gods and goddesses
@main.route('/odin')
def odin():
    return render_template('odin.html')

@main.route('/thor')
def thor():
    return render_template('thor.html')

@main.route('/loki')
def loki():
    return render_template('loki.html')

@main.route('/njord')
def njord():
    return render_template('njord.html')

@main.route('/vili_ve')
def vili_ve():
    return render_template('vili_ve.html')

@main.route('/fjorgyn')
def fjorgyn():
    return render_template('fjorgyn.html')

@main.route('/freyja')
def freyja():
    return render_template('freyja.html')

@main.route('/frigg')
def frigg():
    return render_template('frigg.html')

@main.route('/hel')
def hel():
    return render_template('hel.html')

@main.route('/sif')
def sif():
    return render_template('sif.html')

@main.route('/ragnar_lothbrok')
def ragnar_lothbrok():
    return render_template('ragnar_lothbrok.html')

@main.route('/king_harald_hardrada')
def king_harald_hardrada():
    return render_template('king_harald_hardrada.html')

@main.route('/mjolnir')
def mjolnir():
    return render_template('mjolnir.html')

# ... Add similar routes for other deities ...

# Note: You don't need the following line in this file anymore
# if __name__ == '__main__':
#     app.run(debug=True)

