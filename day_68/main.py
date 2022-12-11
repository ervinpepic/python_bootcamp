from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


login_manager = LoginManager()
login_manager.init_app(app=app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        check_email = User.query.filter_by(email=email).first()
        if check_email:
            flash("This email already exist in the database. Please login!")
            return redirect(url_for("login"))

        hashed_pass = generate_password_hash(
            password=request.form.get("password"), 
            method='pbkdf2:sha256', salt_length=8
            )
        new_user = User(email=email, password=hashed_pass, name=name)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        #get user from the database using email user provided in the form field
        user = User.query.filter_by(email=email).first()

        if user is None:
            error = "Email you entered doesn't exist! Wrong email."
        elif check_password_hash(pwhash=user.password, password=password) == False:
            error = "Wrong password!"
        else: 
            check_password_hash(user.password, password)
            login_user(user)

            return redirect(url_for("secrets"))

    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
