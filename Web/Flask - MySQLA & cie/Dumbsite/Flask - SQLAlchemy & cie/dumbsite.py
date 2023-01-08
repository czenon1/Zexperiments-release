from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy

# port localhost:5000
# Simple Exemple Server
# !!! Folder Tree to build !!!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    login = db.Column(db.String(80))
    desc = db.Column(db.Text)

class UserForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=80)])
    lastname = StringField('Lastname', validators=[InputRequired(), Length(max=80)])
    login = StringField('Login', validators=[InputRequired(), Length(max=80)])
    desc = TextAreaField('Description', validators=[InputRequired()])

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    #return '<h1>HOME Page</h1>'
    return redirect(url_for('index'))

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, lastname=form.lastname.data, login=form.login.data, desc=form.desc.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('list_users'))

@app.route('/showu/<id>')
def show_user(id):
    user = User.query.get(id)
    return render_template('showu.html', user=user)

@app.route('/listu')
def list_users():
    users = User.query.all()
    return render_template('listu.html', users=users)

if __name__ == '__main__':
    app.run()
