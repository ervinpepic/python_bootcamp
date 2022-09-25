from cgitb import html
from operator import methodcaller
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

main_app = Flask(__name__)
Bootstrap(app=main_app)

main_app.config['SECRET_KEY'] = 'asdfasdfasdfdsafewf'

class LoginForm(FlaskForm):
    username = StringField(
        label="Username", 
        name="username", 
        validators=[DataRequired(message="Plese enter your username"), Length(min=3)])

    password = PasswordField(
        label="Password",
        name="password",
        validators=[DataRequired(message="Enter your password"), Length(min=8, message="Please enter at least 8 character long pass")])
    submit = SubmitField(label="Login")

@main_app.route("/")
def home():
    return render_template('index.html')

@main_app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin@admin.com" and form.password.data == "admin1234":
            return render_template('success.html')
        else: 
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    main_app.run(debug=True)