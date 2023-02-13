from flask import Flask
app = Flask(__name__)
print(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</e,>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def bye():
    return "<b>Bye!</b>"

@app.route("/<username>")
def greet(username):
    return f"Hello there {username}!"

if __name__ == '__main__':
    app.run(debug=True)