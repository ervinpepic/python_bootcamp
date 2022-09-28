from enum import unique
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


movie_app = Flask(__name__)


movie_app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


movie_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-ranking.db'
db = SQLAlchemy(app=movie_app)


Bootstrap(movie_app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(220), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(220), unique=False, nullable=False)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return self.title

@movie_app.route("/")
def home():
    movie_list = Movie.query.all()
    return render_template("index.html", movie_list=movie_list)


if __name__ == '__main__':
    movie_app.run(debug=True)
