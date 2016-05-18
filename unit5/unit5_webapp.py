from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveydata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Games(db.Model):
    _tablename_ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    dota = db.Column(db.Boolean)
    lol = db.Column(db.Boolean)
    hots = db.Column(db.Boolean)
    cs = db.Column(db.Boolean)
    cod = db.Column(db.Boolean)
    bf = db.Column(db.Boolean)
    gta = db.Column(db.Boolean)
    fifa = db.Column(db.Boolean)
    minecraft = db.Column(db.Boolean)
    hs = db.Column(db.Boolean)
    sc2 = db.Column(db.Boolean)
    wow = db.Column(db.Boolean)
    other = db.Column(db.Boolean)
    na = db.Column(db.Boolean)
    surveydata_id = db.Column(db.Integer, ForeignKey('surveydata.id'))

    def __init__(self, games_getlist):
        self.dota = 'dota' in games_getlist
        self.lol = 'lol' in games_getlist
        self.hots = 'hots' in games_getlist
        self.cs = 'cs' in games_getlist
        self.cod = 'cod' in games_getlist
        self.bf = 'bf' in games_getlist
        self.gta = 'gta' in games_getlist
        self.fifa = 'fifa' in games_getlist
        self.minecraft = 'minecraft' in games_getlist
        self.hs = 'hs' in games_getlist
        self.sc2 = 'sc2' in games_getlist
        self.wow = 'wow' in games_getlist
        self.other = 'other' in games_getlist
        self.na = 'NA' in games_getlist

class Surveydata(db.Model):
    __tablename__ = 'surveydata'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    education = db.Column(db.String)
    single_multi = db.Column(db.String)
    gametime = db.Column(db.Integer)
    multi_titles = relationship("Games", uselist=False, backref="surveydata")
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


    def __init__(self, gender, age, education, single_multi, gametime, games, communication, resign, resign_freq, resign_choice, salt, salt_self, griefing, griefing_self, guild, guild_why, teamspeak, shyness_factor, reallife_contact, bonding, meeting):
        self.gender = gender
        self.age = age
        self.education = education
        self.single_multi = single_multi
        self.gametime = gametime
        self.multi_titles = games
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
    fd = db.session.query(Surveydata).all()
    return render_template('raw.html', surveydata=fd)

@app.route("/games")
def show_games():
    fd = db.session.query(Games).all()
    return render_template('games.html', surveydata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Surveydata).all()
    females = Surveydata.query.filter_by(gender='F').count()
    males = Surveydata.query.filter_by(gender='M').count()
    gender_list = [females, males]

    ageGroup1 = Surveydata.query.filter_by(age=1).count()
    ageGroup2 = Surveydata.query.filter_by(age=2).count()
    ageGroup3 = Surveydata.query.filter_by(age=3).count()
    ageGroup4 = Surveydata.query.filter_by(age=4).count()
    ageGroup5 = Surveydata.query.filter_by(age=5).count()
    ageGroup_list = [ageGroup1, ageGroup2, ageGroup3, ageGroup4, ageGroup5]

    educationGroup1 = Surveydata.query.filter_by(education=1).count()
    educationGroup2 = Surveydata.query.filter_by(education=2).count()
    educationGroup3 = Surveydata.query.filter_by(education=3).count()
    educationGroup4 = Surveydata.query.filter_by(education=4).count()
    educationGroup_list =[educationGroup1, educationGroup2, educationGroup3, educationGroup4]

    single = Surveydata.query.filter_by(single_multi='sp').count()
    multi = Surveydata.query.filter_by(single_multi='mp').count()
    single_multi = Surveydata.query.filter_by(single_multi='msp').count()
    smp_list = [single, multi, single_multi]

    gametimeGroup1 = Surveydata.query.filter_by(education=1).count()
    gametimeGroup2 = Surveydata.query.filter_by(education=2).count()
    gametimeGroup3 = Surveydata.query.filter_by(education=3).count()
    gametimeGroup4 = Surveydata.query.filter_by(education=4).count()
    gametimeGroup5 = Surveydata.query.filter_by(education=5).count()
    gametimeGroup_list = [gametimeGroup1,gametimeGroup2,gametimeGroup3,gametimeGroup4,gametimeGroup5]
    return render_template('result.html', data=fd_list, gender=gender_list, ageGroup=ageGroup_list, educationGroup=educationGroup_list, smp=smp_list, gametimeGroup=gametimeGroup_list)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM6
    gender = request.form['gender']
    age = request.form['age']
    education = request.form['education']
    single_multi = request.form['single_multi']
    gametime = request.form['gametime']
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

    # Checkbox Form data
    games = request.form.getlist('multi_titles[]')

    # Save the data
    games_dbRow = Games(games)
    survey_dbRow = Surveydata(gender, age, education, single_multi, gametime, games_dbRow, communication, resign, resign_freq, resign_choice, salt, salt_self, griefing, griefing_self, guild, guild_why, teamspeak, shyness_factor, reallife_contact, bonding, meeting)

    db.session.add(survey_dbRow)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()