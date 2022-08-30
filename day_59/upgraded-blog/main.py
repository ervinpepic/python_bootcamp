from email import message
from flask import Flask, render_template, request
import requests
import smtplib

server_email = "@gmail.com"
server_password = "apppassword"
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


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=server_email, password=server_password)
            connection.sendmail(from_addr=server_email, to_addrs=data['email'],
            msg=f"""Subject:Contact page\n\n

                Person: {data['name']}
                Phone: {data['phone']}

                Message: {data['message']}
            """)
        return render_template(template_name_or_list="contact.html", message_success=True)
    return render_template(template_name_or_list="contact.html", message_success=False)

@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for single_post in posts_array:
        if single_post["id"] == index:
            requested_post = single_post
    return render_template(template_name_or_list="post.html", post=requested_post)
    

if __name__ == "__main__":
    app.run(debug=True)