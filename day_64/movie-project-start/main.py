from enum import unique
from turtle import title
from urllib import response
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

MOVIE_API_KEY = "/"
MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_URL_DETAILS = "https://api.themoviedb.org/3/movie"

movie_app = Flask(__name__)


movie_app.config['SECRET_KEY'] = '/'


movie_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-ranking.db'
db = SQLAlchemy(app=movie_app)


Bootstrap(movie_app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(220), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(220), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return self.title


class RateMovieForm(FlaskForm):
    rating_update = FloatField(label="Edit movie rating", validators=[DataRequired()])
    review_update = StringField(label="Edit movie review", validators=[DataRequired()])
    submit = SubmitField("Update movie info")

class AddMovieForm(FlaskForm):
    title = StringField(label="Enter movie title", validators=[DataRequired()])
    submit = SubmitField("Add new movie")


@movie_app.route("/")
def home():
    movie_list = Movie.query.order_by(Movie.rating.desc()).all()
    return render_template("index.html", movie_list=movie_list)

@movie_app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        params = {
        "api_key": MOVIE_API_KEY,
        "query": movie_title,
        }
        response = requests.get(MOVIE_URL, params=params)
        movies = response.json()["results"]
        return render_template("select.html", movies=movies)
    return render_template('add.html', form=form)


@movie_app.route("/find")
def find():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        url = f"{MOVIE_URL_DETAILS}/{movie_api_id}"
        params = {
        "api_key": MOVIE_API_KEY,
        }
        response = requests.get(url=url, params=params)
        movie_details = response.json()
        new_movie = Movie(
            title=movie_details["title"],
            year=movie_details["release_date"].split("-")[0],
            img_url=f"{'https://image.tmdb.org/t/p/w500/'}{movie_details['poster_path']}",
            description=movie_details["overview"]
            )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


@movie_app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = form.rating_update.data
        movie_to_update.review = form.review_update.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_update)


@movie_app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    movie_app.run(debug=True)
