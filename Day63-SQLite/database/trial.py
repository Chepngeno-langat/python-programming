from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from yourapplication import db

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
local_user = User(username='local_user', email='user@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()
