from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

app = Flask(__name__)
app.secret_key = "karen-langat"

@app.route('/')
def index():
    user_info = {
        'name':'User'
    }
    return render_template('index.html', user=user_info)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.user_name.data == 'admin' and form.password.data == 'admin':
            flash('login successful')
            return redirect('index')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)