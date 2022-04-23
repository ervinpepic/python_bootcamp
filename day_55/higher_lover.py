import random
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Gues a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

random_num = random.randint(0, 9)

@app.route("/<int:num>")
def guess(num):
    if num > random_num:
        return '<h1>Too high, try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < random_num:
        return '<h1>Too low, try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif num == random_num:
        return '<h1>You found me!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)