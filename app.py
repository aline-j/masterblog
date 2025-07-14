from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)
DATA_FILE = 'blog_posts.json'


# Load blog posts from the JSON file
def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


# Save blog posts to the JSON file
def save_posts(posts):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


# Index Route
@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        pass
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)