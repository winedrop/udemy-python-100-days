from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    open = StringField('open-time', validators=[DataRequired()])
    close = StringField('close-time', validators=[DataRequired()])
    coffee = SelectField('coffee-rating', validators=[DataRequired()],choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕'])
    wifi = SelectField('wifi-rating', validators=[DataRequired()],choices=['💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'])
    socket = SelectField('socket-availability', validators=[DataRequired()], choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("true")
        row_data = []
        row_data.append(form.cafe.data)
        row_data.append(form.location.data)
        row_data.append(form.open.data)
        row_data.append(form.close.data)
        row_data.append(form.coffee.data)
        row_data.append(form.wifi.data)
        
        with open('62_bootstrapflask_WTForms/static/cafe-data.csv', 'a') as csv_file:
            csv_file.write('\n')
            for column in row_data:
                csv_file.write(column + ", ")
            csv_file.write(form.socket.data)
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('62_bootstrapflask_WTForms/static/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
