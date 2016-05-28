# Load required modules, configure database, db class definitions
from backend_config import *

def count_num_queries(list, classname, maxCounter):
    counter = 1
    while (counter <= maxCounter):
        if(classname == "age"):
            list.append(Surveydata.query.filter_by(age=counter).count())
        elif(classname == "education"):
            list.append(Surveydata.query.filter_by(education=counter).count())
        elif(classname == "gametime"):
            list.append(Surveydata.query.filter_by(gametime=counter).count())
        elif(classname == "resign"):
            list.append(Surveydata.query.filter_by(resign_freq=counter).count())
        else:
            break
        counter = counter + 1
    return list

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
    fd_list = db.session.query(Games).all()

    females = Surveydata.query.filter_by(gender='F').count()
    males = Surveydata.query.filter_by(gender='M').count()
    gender_list = [females, males]


    ageGroup_list = []
    count_num_queries(ageGroup_list,"age", 5)

    educationGroup_list = []
    count_num_queries(educationGroup_list,"education",4)

    gametimeGroup_list = []
    count_num_queries(gametimeGroup_list,"gametime",5)


    single = Surveydata.query.filter_by(single_multi='sp').count()
    multi = Surveydata.query.filter_by(single_multi='mp').count()
    single_multi = Surveydata.query.filter_by(single_multi='msp').count()
    smp_list = [single, multi, single_multi]



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

    resignGroup_list = []
    resignGroup_list.append(Surveydata.query.filter_by(resign="no").count())
    count_num_queries(resignGroup_list,"resign",5)

    resignChoiceGroup1 = Resign.query.filter_by(sport=True).count()
    resignChoiceGroup2 = Resign.query.filter_by(family=True).count()
    resignChoiceGroup3 = Resign.query.filter_by(friends=True).count()
    resignChoiceGroup4 = Resign.query.filter_by(chores=True).count()
    resignChoiceGroup5 = Resign.query.filter_by(work=True).count()
    resignChoiceGroup6 = Resign.query.filter_by(other=True).count()
    resignChoiceGroup_list = [resignChoiceGroup1,resignChoiceGroup2,resignChoiceGroup3,resignChoiceGroup4,resignChoiceGroup5,resignChoiceGroup6]

    guild = Surveydata.query.filter_by(guild="no").count()
    guildWhy1 = Guild.query.filter_by(meeting=True).count()
    guildWhy2 = Guild.query.filter_by(team=True).count()
    guildWhy3 = Guild.query.filter_by(benefits=True).count()
    guildWhy4 = Guild.query.filter_by(other=True).count()
    guildWhy_list = [guild, guildWhy1, guildWhy2, guildWhy3, guildWhy4]

    Salt = Surveydata.query.filter_by(salt="yes").count()
    SaltNo = Surveydata.query.filter_by(salt="no").count()
    SaltSelf = Surveydata.query.filter_by(salt_self="yes").count()
    Griefing = Surveydata.query.filter_by(griefing="yes").count()
    GriefingSelf = Surveydata.query.filter_by(griefing_self="yes").count()
    GriefingNo = Surveydata.query.filter_by(griefing="no").count()
    Salt_list =[Salt, SaltNo, SaltSelf, Griefing, GriefingSelf, GriefingNo]


    ShynessFactor = Surveydata.query.filter_by(shyness_factor="yes").count()
    ReallifeContact = Surveydata.query.filter_by(reallife_contact="yes").count()
    Bonding = Surveydata.query.filter_by(bonding="yes").count()
    Meeting = Surveydata.query.filter_by(meeting="yes").count()

    Communication_list =[ShynessFactor, ReallifeContact, Bonding, Meeting]

    return render_template('result.html', communication=Communication_list, salt=Salt_list, guildWhy=guildWhy_list, resignChoice=resignChoiceGroup_list, resign=resignGroup_list,  gt=gt_list, data=fd_list, gender=gender_list, ageGroup=ageGroup_list, educationGroup=educationGroup_list, smp=smp_list, gametimeGroup=gametimeGroup_list)


def isFieldNA(fieldname, resultType = 'string'):
    if (fieldname in request.form):
        return request.form[fieldname]
    else:
        if(resultType == 'string'):
            return 'NA'
        if(resultType == 'int'):
            return -1

@app.route("/save", methods=['POST'])
def save():
    # Get data from form
    try:
        gender = request.form['gender']
        age = request.form['age']
        education = request.form['education']
        single_multi = request.form['single_multi']
        gametime = request.form['gametime']
        communication = request.form['communication']
        resign = request.form['resign']
    except KeyError:
        return redirect('/form?error=true')

    resign_freq = isFieldNA('resign_freq', 'int')
    salt = isFieldNA('salt')
    salt_self = isFieldNA('salt_self')
    griefing = isFieldNA('griefing')
    griefing_self = isFieldNA('griefing_self')
    guild = isFieldNA('guild')
    teamspeak = isFieldNA('teamspeak')
    shyness_factor = isFieldNA('shyness_factor')
    reallife_contact = isFieldNA('reallife_contact')
    bonding = isFieldNA('bonding')
    meeting = isFieldNA('meeting')

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