from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

WTF_CSRF_SECRET_KEY = 'a random string'

app = Flask(__name__)
app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY

# wtforms
class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        if form.validate_on_submit():
            return success()
            pass
        else:
            return denied()

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')


def authenticate():
    if request.method == 'POST':
        return render_template("login.html")
    else :
        return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)