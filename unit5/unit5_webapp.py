from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveydata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'surveydata'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    education = db.Column(db.String)
    single_multi = db.Column(db.String)
    gametime = db.Column(db.Integer)
    multi_titles = db.Column(db.String)
    communication = db.Column(db.String)
    resign = db.Column(db.String)
    resign_freq = db.Column(db.Integer)
    resign_choice = db.Column(db.String)
    salt = db.Column(db.String)
    salt_self = db.Column(db.String)
    griefing = db.Column(db.String)
    griefing_self = db.Column(db.String)
    guild = db.Column(db.String)
    guild_why = db.Column(db.String)
    teamspeak = db.Column(db.String)
    shyness_factor = db.Column(db.String)
    reallife_contact = db.Column(db.String)
    bonding = db.Column(db.String)
    meeting = db.Column(db.String)


    def __init__(self, gender, age, education, single_multi, gametime, multi_titles, communication, resign, resign_freq, resign_choice, salt, salt_self, griefing, griefing_self, guild, guild_why, teamspeak, shyness_factor, reallife_contact, bonding, meeting):
        self.gender = gender
        self.age = age
        self.education = education
        self.single_multi = single_multi
        self.gametime = gametime
        self.multi_titles = multi_titles
        self.communication = communication
        self.resign = resign
        self.resign_freq = resign_freq
        self.resign_choice = resign_choice
        self.salt = salt
        self.salt_self = salt_self
        self.griefing = griefing
        self.griefing_self = griefing_self
        self.guild = guild
        self.guild_why = guild_why
        self.teamspeak = teamspeak
        self.shyness_factor = shyness_factor
        self.reallife_contact = reallife_contact
        self.bonding = bonding
        self.meeting = meeting

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', surveydata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions


    return render_template('result.html', data=data)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    gender = request.form['gender']
    age = request.form['age']
    education = request.form['education']
    single_multi = request.form['single_multi']
    gametime = request.form['gametime']
    multi_titles = request.form['multi_titles[]']
    communication = request.form['communication']
    resign = request.form['resign']
    resign_freq = request.form['resign_freq']
    resign_choice = request.form['resign_choice[]']
    salt = request.form['salt']
    salt_self = request.form['salt_self']
    griefing = request.form['griefing']
    griefing_self = request.form['griefing_self']
    guild = request.form['guild']
    guild_why = request.form['guild_why[]']
    teamspeak = request.form['teamspeak']
    shyness_factor = request.form['shyness_factor']
    reallife_contact = request.form['reallife_contact']
    bonding = request.form['bonding']
    meeting = request.form['meeting']


    # Save the data
    fd = Formdata(gender, age, education, single_multi, gametime, multi_titles, communication, resign, resign_freq, resign_choice, salt, salt_self, griefing, griefing_self, guild, guild_why, teamspeak, shyness_factor, reallife_contact, bonding, meeting)

    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()