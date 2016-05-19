# Load required modules, configure database, db class definitions
from backend_config import *


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

@app.route("/resign")
def show_resign():
    fd = db.session.query(Resign).all()
    return render_template('resign.html', surveydata=fd)

@app.route("/guild")
def show_guild():
    fd = db.session.query(Guild).all()
    return render_template('guild.html', surveydata=fd)

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

    gametimeGroup1 = Surveydata.query.filter_by(gametime=1).count()
    gametimeGroup2 = Surveydata.query.filter_by(gametime=2).count()
    gametimeGroup3 = Surveydata.query.filter_by(gametime=3).count()
    gametimeGroup4 = Surveydata.query.filter_by(gametime=4).count()
    gametimeGroup5 = Surveydata.query.filter_by(gametime=5).count()
    gametimeGroup_list = [gametimeGroup1,gametimeGroup2,gametimeGroup3,gametimeGroup4,gametimeGroup5]

    gtDOTA = Games.query.filter_by(dota=True).count()
    gtLOL = Games.query.filter_by(lol=True).count()
    gtHOTS = Games.query.filter_by(hots=True).count()
    gtCS = Games.query.filter_by(cs=True).count()
    gtCOD = Games.query.filter_by(cod=True).count()
    gtBF = Games.query.filter_by(bf=True).count()
    gtGTA = Games.query.filter_by(gta=True).count()
    gtFIFA = Games.query.filter_by(fifa=True).count()
    gtMC = Games.query.filter_by(minecraft=True).count()
    gtHS = Games.query.filter_by(hs=True).count()
    gtSC2 = Games.query.filter_by(sc2=True).count()
    gtWOW = Games.query.filter_by(wow=True).count()
    gtOTHER = Games.query.filter_by(other=True).count()
    gt_list = [gtDOTA, gtLOL, gtHOTS, gtCS, gtCOD, gtBF, gtGTA, gtFIFA, gtMC, gtHS, gtSC2, gtWOW, gtOTHER]

    resignGroup1 = Surveydata.query.filter_by(resign="no").count()
    resignGroup2 = Surveydata.query.filter_by(resign_freq=1).count()
    resignGroup3 = Surveydata.query.filter_by(resign_freq=2).count()
    resignGroup4 = Surveydata.query.filter_by(resign_freq=3).count()
    resignGroup5 = Surveydata.query.filter_by(resign_freq=4).count()
    resignGroup6 = Surveydata.query.filter_by(resign_freq=5).count()
    resignGroup_list = [resignGroup1, resignGroup2, resignGroup3, resignGroup4, resignGroup5, resignGroup6]

    resignChoiceGroup1 = Resign.query.filter_by(sport=True).count()
    resignChoiceGroup2 = Resign.query.filter_by(family=True).count()
    resignChoiceGroup3 = Resign.query.filter_by(friends=True).count()
    resignChoiceGroup4 = Resign.query.filter_by(chores=True).count()
    resignChoiceGroup5 = Resign.query.filter_by(work=True).count()
    resignChoiceGroup6 = Resign.query.filter_by(other=True).count()
    resignChoiceGroup_list = [resignChoiceGroup1,resignChoiceGroup2,resignChoiceGroup3,resignChoiceGroup4,resignChoiceGroup5,resignChoiceGroup6]


    return render_template('result.html', resignChoice=resignChoiceGroup_list, resign=resignGroup_list,  gt=gt_list, data=fd_list, gender=gender_list, ageGroup=ageGroup_list, educationGroup=educationGroup_list, smp=smp_list, gametimeGroup=gametimeGroup_list)


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
    salt = request.form['salt']
    salt_self = request.form['salt_self']
    griefing = request.form['griefing']
    griefing_self = request.form['griefing_self']
    guild = request.form['guild']
    teamspeak = request.form['teamspeak']
    shyness_factor = request.form['shyness_factor']
    reallife_contact = request.form['reallife_contact']
    bonding = request.form['bonding']
    meeting = request.form['meeting']

    # Checkbox Form data
    multi_titles = request.form.getlist('multi_titles[]')
    resign_choice = request.form.getlist('resign_choice[]')
    guild_why = request.form.getlist('guild_why[]')

    # Save the data
    games_dbRow = Games(multi_titles)
    resign_dbRow = Resign(resign_choice)
    guild_dbRow = Guild(guild_why)
    survey_dbRow = Surveydata(gender, age, education, single_multi, gametime, games_dbRow, communication, resign, resign_freq, resign_dbRow, salt, salt_self, griefing, griefing_self, guild, guild_dbRow, teamspeak, shyness_factor, reallife_contact, bonding, meeting)

    db.session.add(survey_dbRow)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()