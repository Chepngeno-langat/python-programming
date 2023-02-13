from flask import Flask
app = Flask(__name__)

import random

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9.</h1>" \
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"

@app.route("/<int:guess>")
@app.route('/<user_number>')
def guess_number(guess):
    if guess > random_number:
        return f"Oops! {guess} is too high!" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return f"{guess} is too low, Try again" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    else:
        return f"Correct!" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == '__main__':
    app.run(debug=True)