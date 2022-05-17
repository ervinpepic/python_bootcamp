from flask import Flask, render_template
import requests
posts_array = []

response = requests.get(url="https://api.npoint.io/45847e37f040db0a39e6").json()
for post in response:
    posts_array.append(post)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(template_name_or_list="index.html", posts=posts_array)

@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")


@app.route("/contact")
def contact():
    return render_template(template_name_or_list="contact.html")

@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for single_post in posts_array:
        if single_post["id"] == index:
            requested_post = single_post
    return render_template(template_name_or_list="post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)