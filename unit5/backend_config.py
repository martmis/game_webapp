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


class Resign(db.Model):
    _tablename_ = 'resign'
    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.Boolean)
    family = db.Column(db.Boolean)
    friends = db.Column(db.Boolean)
    chores = db.Column(db.Boolean)
    work = db.Column(db.Boolean)
    other = db.Column(db.Boolean)
    na = db.Column(db.Boolean)
    surveydata_id = db.Column(db.Integer, ForeignKey('surveydata.id'))

    def __init__(self, resign_getlist):
        self.sport = 'sport' in resign_getlist
        self.family = 'family' in resign_getlist
        self.friends = 'friends' in resign_getlist
        self.chores = 'chores' in resign_getlist
        self.work = 'work' in resign_getlist
        self.other = 'other' in resign_getlist
        self.na = 'NA' in resign_getlist


class Guild(db.Model):
    _tablename_ = 'guild'
    id = db.Column(db.Integer, primary_key=True)
    meeting = db.Column(db.Boolean)
    team = db.Column(db.Boolean)
    benefits = db.Column(db.Boolean)
    other = db.Column(db.Boolean)
    na = db.Column(db.Boolean)
    surveydata_id = db.Column(db.Integer, ForeignKey('surveydata.id'))

    def __init__(self, guild_getlist):
        self.meeting = 'meeting' in guild_getlist
        self.team = 'team' in guild_getlist
        self.benefits = 'benefits' in guild_getlist
        self.other = 'other' in guild_getlist
        self.na = 'NA' in guild_getlist


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
    resign_choice = relationship("Resign", uselist=False, backref="surveydata")
    salt = db.Column(db.String)
    salt_self = db.Column(db.String)
    griefing = db.Column(db.String)
    griefing_self = db.Column(db.String)
    guild = db.Column(db.String)
    guild_why = relationship("Guild", uselist=False, backref="surveydata")
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