from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
from flask import Flask  # Add this line to import Flask

import sqlite3
from datetime import datetime

main = Blueprint('main', __name__)
app = Flask(__name__)  # Create an instance of Flask

@main.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    formatted_posts = []
    for post in posts:
        created = datetime.strptime(post['created'], '%Y-%m-%d %H:%M:%S')
        formatted_post = {
            'id': post['id'],
            'title': post['title'],
            'content': post['content'],
            'created': created.strftime('%B %d, %Y')
        }
        formatted_posts.append(formatted_post)

    print(formatted_posts)  # Add this line to check the value of formatted_posts

    return render_template('index.html', posts=formatted_posts)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()

    if post is None:
        abort(404)

    return post

@main.route('/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@main.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            flash('Post created successfully!', 'success')
            return redirect(url_for('main.index'))

    return render_template('create.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
            conn.commit()
            conn.close()
            flash('Post updated successfully!', 'success')
            return redirect(url_for('main.index'))

    return render_template('edit.html', post=post)

@main.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/research')
def research():
    posts = get_all_posts()
    return render_template('research.html', posts=posts)

research = Blueprint('research', __name__)

@research.route('/research-postings')
def research_postings():
    posts = get_all_posts()
    return render_template('research_postings.html', posts=posts)

def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts
