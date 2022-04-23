from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@app.route('/')
def hello_world():
    return "Hello world"


@app.route("/bye")
@make_bold
def bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)