from enum import unique
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
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


class RateMovieForm(FlaskForm):
    rating_update = FloatField(label="Edit movie rating", validators=[DataRequired()])
    review_update = StringField(label="Edit movie review", validators=[DataRequired()])
    submit = SubmitField("Update movie info")


@movie_app.route("/")
def home():
    movie_list = Movie.query.all()
    return render_template("index.html", movie_list=movie_list)


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
