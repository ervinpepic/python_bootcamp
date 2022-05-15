from datetime import datetime
import random
import requests
from flask import Flask, render_template

GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"


app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("/index.html", number=random_number, year=current_year)


@app.route('/guess/<string:name>')
def guess(name):
    params = {
    "name": name
    }
    genderize = requests.get(url=GENDERIZE_URL, params=params)
    gender_response = genderize.json()["gender"]
    gender = gender_response

    agify = requests.get(url=AGIFY_URL, params=params)
    agify_response = agify.json()["age"]
    age = agify_response
    return render_template("gues.html", age=age, name=name.capitalize(), gender=gender)
    
@app.route("/blog/<int:id>")
def get_blog(id):
    blog_url = "https://api.npoint.io/45847e37f040db0a39e6"
    resp = requests.get(url=blog_url)
    all_posts = resp.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)