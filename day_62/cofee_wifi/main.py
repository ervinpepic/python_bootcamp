from crypt import methods
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

main_app = Flask(__name__)
main_app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(main_app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL(require_tld=True)])
    open_time = StringField('Open', validators=[DataRequired()])
    close_time = StringField('Close', validators=[DataRequired()])
    coffee = SelectField("Cofee Rating", validators=[DataRequired()], 
        choices=["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕"])
    wifi = SelectField("Wifi Strength Rating", validators=[DataRequired()], 
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪"])
    power = SelectField('Power Socket Availability', validators=[DataRequired()],
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

# all Flask routes below
@main_app.route("/")
def home():
    return render_template("index.html")


@main_app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        form_data = [
            form.cafe.data,
            form.location.data,
            form.open_time.data,
            form.close_time.data,
            form.coffee.data,
            form.wifi.data,
            form.power.data
        ]
        with open(r'cafe-data.csv', mode='a', newline='') as write_into_csv:
            writer = csv.writer(write_into_csv)
            writer.writerow(form_data)
    return render_template('add.html', form=form)


@main_app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    main_app.run(debug=True)
