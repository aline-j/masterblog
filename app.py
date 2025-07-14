from flask import Flask, request, render_template, redirect, url_for
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

# Add Route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = load_posts()
        # Collect all IDs
        ids = []
        for post in posts:
            ids.append(post['id'])
        # Determine next ID
        if ids:
            new_id = max(ids) + 1
        else:
            new_id = 1

        new_post = {
            'id': new_id,
            'author': request.form.get('author'),
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }

        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('add.html')

# Delete Route
@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()

    filtered_posts = []
    for post in posts:
        if post["id"] != post_id:
            filtered_posts.append(post)

    save_posts(filtered_posts)
    return redirect(url_for('index'))

# Update Route
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    posts = load_posts()

    # Search post
    post = None
    for post_in_list in posts:
        if post_in_list["id"] == post_id:
            post = post_in_list
            break

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Form has been submitted → Update data
        post["author"] = request.form.get("author")
        post["title"] = request.form.get("title")
        post["content"] = request.form.get("content")
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)