from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = 'blog_posts.json'


# Load blog posts from JSON file
def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


# Save blog posts to JSON file
def save_posts(posts):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4)


# Route to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = load_posts()
    return jsonify(posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)