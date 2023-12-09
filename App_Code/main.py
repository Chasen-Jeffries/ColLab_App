from flask import Flask, Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
import sqlite3
import openai

app = Flask(__name__)

# Your OpenAI API key
import os

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("No OpenAI API key set for 'OPENAI_API_KEY' environment variable")
openai.api_key = openai_api_key

# Blueprint for the main part of the application
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

# To Create Myth
@main.route('/create_myth', methods=['GET', 'POST'])
def create_myth():
    # Route logic here
    return render_template('create_myth.html')

# Individual post route
@main.route('/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# Create post route
@main.route('/create_post', methods=['GET', 'POST'])  # Changed route to avoid conflict
@login_required
def create_post():
    # ... existing create post logic ...
    return render_template('create_post.html')  # Assuming you have a separate template for creating posts

# Edit post route
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = get_post(id)  # Fetch the post to be edited
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
    query = request.args.get('query')  # Assuming you're getting a query parameter
    matching_posts = []  # Replace with actual logic to get matching posts
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

# Register the Blueprint with the app
app.register_blueprint(main, url_prefix='/')

# OpenAI Myth Creation Route
@app.route('/create_myth', methods=['GET', 'POST'])  # Changed route to avoid conflict
def create_myth():
    if request.method == 'POST':
        try:
            title = request.form['title']
            realms = request.form['realms']
            gods = request.form['gods']
            creatures = request.form['creatures']
            print(title, realms, gods, creatures)  # Debugging line
            myth = generate_myth(title, realms, gods, creatures)
            return render_template('myth.html', myth=myth)
        except Exception as e:
            print(f"Error: {e}")
            return render_template('error.html', error=e)
    return render_template('create_myth.html')  # Assuming you have a separate template for creating myths

def generate_myth(title, realms, gods, creatures):
    prompt = f"Create a myth with the title '{title}', set in {realms}, involving gods and goddesses like {gods}, and featuring creatures such as {creatures}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    print(response)  # Debugging line
    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run(debug=True)

