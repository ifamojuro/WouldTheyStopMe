from flask import render_template, send_file,request
from .app import (app,pd,data,rows,boston_data,bos_rows,phili_data, phili_rows, la_data, la_rows,
noladata,nola_rows)


def ny_filter_data(race,sex,age,hair,eye):
    race = [race]
    sex = [sex]
    age = age
    hair = [hair]
    eye = [eye]

    if race[0] == "None":
        race = list(data.race.unique())
    if sex[0] == "None":
        sex = list(data.sex.unique())
    if hair[0] == "None":
        hair = list(data.haircolr.unique())
    if eye[0] == "None":
        eye = list(data.eyecolor.unique())
    age_range = age.split(',')
    stops = data[(data['sex'].isin(sex)) & (data['race'].isin(race)) & (data['haircolr'].isin(hair)) & (data['eyecolor'].isin(eye))]

    if age_range[0]!="None":
        stops = stops[(stops['age'] >= age_range[0]) & (stops['age'] <= age_range[1])]

    return stops

def bos_filter_data(race,sex,age,hair,eth,comp):
    race = [race]
    sex = [sex]
    age = age
    hair = [hair]
    eth = [eth]
    comp = [comp]

    if race[0] == "None":
        race = list(boston_data.race.unique())
    if sex[0] == "None":
        sex = list(boston_data.sex.unique())
    if hair[0] == "None":
        hair = list(boston_data.hair_style.unique())
    if eth[0] == "None":
        eth = list(boston_data.ethnicity.unique())
    if comp[0] == "None":
        comp= list(boston_data.complexion.unique())
    
    age_range = age.split(',')

    stops = boston_data[(boston_data['sex'].isin(sex)) & (boston_data['race'].isin(race)) & (boston_data['hair_style'].isin(hair)) & (boston_data['ethnicity'].isin(eth)) 
        & (boston_data['complexion'].isin(comp))]

    if age_range[0]!="None":
        stops = stops[(stops['age'] >= int(age_range[0])) & (stops['age'] <= int(age_range[1]))]

    return stops

def phili_filter_data(race,sex,age,stop):
    race = [race]
    sex = [sex]
    age = age
    stop = [stop]
 

    if race[0] == "None":
        race = list(phili_data.race.unique())
    if sex[0] == "None":
        sex = list(phili_data.gender.unique())
    if stop[0] == "None":
        hair = list(phili_data.stoptype.unique())
    
    age_range = age.split(',')

    stops = phili_data[(phili_data['gender'].isin(sex)) & (phili_data['race'].isin(race)) & (phili_data['stoptype'].isin(stop))]

    if age_range[0]!="None":
        stops = stops[(stops['age'] >= int(age_range[0])) & (stops['age'] <= int(age_range[1]))]

    return stops

def nola_filter_data(race,sex,age,hair,eye):
    race = [race]
    sex = [sex]
    age = age
    hair = [hair]
    eye = [eye]

    if race[0] == "None":
        race = list(noladata.SubjectRace.unique())
    if sex[0] == "None":
        sex = list(noladata.SubjectGender.unique())
    if hair[0] == "None":
        hair = list(noladata.SubjectHairColor.unique())
    if eye[0] == "None":
        eye = list(noladata.SubjectEyeColor.unique())
    age_range = age.split(',')

    stops = noladata[(noladata['SubjectGender'].isin(sex)) & (noladata['SubjectRace'].isin(race)) & (noladata['SubjectHairColor'].isin(hair)) & (noladata['SubjectEyeColor'].isin(eye))]
    #stops = data[(data['sex'].isin(sex)) & (data['race'].isin(race)) & (data['haircolr'].isin(hair)) & (data['eyecolor'].isin(eye))]

    if age_range[0]!="None":
        stops = stops[(stops['SubjectAge'] >= age_range[0]) & (stops['SubjectAge'] <= age_range[1])]

    return stops

def la_filter_data(race,sex,stop):
    race = [race]
    sex = [sex] 
    stop = [stop]

    if race[0] == "None":
        race = list(la_data.Descent_Description.unique())
    if sex[0] == "None":
        sex = list(la_data.Sex_Code.unique())
    if stop[0] == "None":
        stop = list(la_data.Stop_Type.unique())

    stops = la_data[(la_data['Sex_Code'].isin(sex)) & (la_data['Descent_Description'].isin(race)) & (la_data['Stop_Type'].isin(stop))]

    return stops


def pctize(part,whole):
    return round((part/(whole* 1.0)) * 100)

def sit_pct(data,col):
    x = data[col].value_counts()
    x_y=int(x["Y"])
    return pctize(x_y,len(data))

@app.route("/")
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("home.html")

@app.route("/new_york_form")
def ny_data():
    if request.method == 'GET':
        race = request.args.get("race") 
        sex = request.args.get("sex")
        age = request.args.get("age")
        hair = request.args.get("haircolr")
        eye = request.args.get("eyecolor")
        stops = ny_filter_data(race,sex,age,hair,eye)
        stops_num = len(stops)
        stops_percentage = round((stops_num/(rows * 1.0)) * 100)
        dept = "New York City Police Department"
        return render_template("results.html", stops_num=stops_num, stops_perc=stops_percentage, rows=rows,
            race=race,sex=sex,age=age,hair=hair,eye=eye, dept=dept)

@app.route("/Boston_Form")
def boston_filter():
    if request.method == 'GET':
        race = request.args.get("race") 
        sex = request.args.get("sex")
        age = request.args.get("age")
        hair = request.args.get("hair_style")
        eth = request.args.get("ethnicity")
        comp = request.args.get("complexion")
        stops = bos_filter_data(race,sex,age,hair,eth,comp)
        stops_num = len(stops)
        stops_percentage = round((stops_num/(bos_rows * 1.0)) * 100)
        dept = "Boston Police Department"
        return render_template("results.html", stops_num=stops_num, stops_perc=stops_percentage, rows=bos_rows,
            race=race,sex=sex,age=age, dept=dept)

@app.route("/Phili_Form")
def phili_filter():
    if request.method == 'GET':
        race = request.args.get("race") 
        sex = request.args.get("sex")
        age = request.args.get("age")
        stop = request.args.get("stop_type")
        stops = phili_filter_data(race,sex,age,stop)
        stops_num = len(stops)
        stops_percentage = round((stops_num/(phili_rows * 1.0)) * 100)
        dept = "Philidelphia Police Department"
        return render_template("results.html", stops_num=stops_num, stops_perc=stops_percentage, rows=phili_rows,
            race=race,sex=sex,age=age, dept=dept)

@app.route("/new_orelans_form")
def nola_data():
    if request.method == 'GET':
        race = request.args.get("race") 
        sex = request.args.get("sex")
        age = request.args.get("age")
        hair = request.args.get("haircolr")
        eye = request.args.get("eyecolor")
        stops = nola_filter_data(race,sex,age,hair,eye)
        stops_num = len(stops)
        stops_percentage = round((stops_num/(nola_rows * 1.0)) * 100)
        dept = "New Orleans Police Department"
        return render_template("results.html", stops_num=stops_num, stops_perc=stops_percentage, rows=nola_rows,
            race=race,sex=sex,age=age,hair=hair,eye=eye, dept=dept)

@app.route("/las_angeles_form")
def la_data_analysis():
    if request.method == 'GET':
        race = request.args.get("descent") 
        sex = request.args.get("sex")
        typ = request.args.get("stop_type")
        stops = la_filter_data(race,sex,typ)
        stops_num = len(stops)
        stops_percentage = round((stops_num/(la_rows * 1.0)) * 100)
        dept = "Las Angeles Police Department"
        return render_template("results.html", stops_num=stops_num, stops_perc=stops_percentage, rows=la_rows,
            race=race,sex=sex,dept=dept)


@app.route("/data")
def data_show():
    return render_template("data.html")

@app.route("/data_download/<city>")
def data_download(city):
    if city == "NYC":
        return send_file("static/data/raw_data.csv", attachment_filename='nypd_data_2016.csv', as_attachment=True)
    if city == "BOS":
        return send_file("static/data/boston_data_1.csv", attachment_filename='bos_data_2016.csv', as_attachment=True)
    if city == "PHI":
        return send_file("static/data/phili_2016.csv", attachment_filename='phi_data_2016.csv', as_attachment=True)
    if city == "NOLA":
        return send_file("static/data/nola_2016.csv", attachment_filename='nola_data_2016.csv', as_attachment=True)
"""
@app.route("/more_details/<ent>/<race>/<sex>/<age>/<hair>/<eye>")
def more_details(ent,race,sex,age,hair,eye):
    stops=filter_data(race,sex,age,hair,eye)
    without = data[~data.isin(stops)].dropna()
    stops_num = len(stops)

    #Get situational data_profile

    prof_sit_data = {
    "explnstp": sit_pct(stops,"explnstp"),
    "frisked": sit_pct(stops,"frisked"),
    "searched": sit_pct(stops,"searched"),
    "contrabn": sit_pct(stops,"contrabn"),
    "arstmade": sit_pct(stops,"arstmade")
    }
    print(prof_sit_data)

    #Get situational all_data
    all_sit_data = {
    "explnstp": sit_pct(without,"explnstp"),
    "frisked": sit_pct(without,"frisked"),
    "searched": sit_pct(without,"searched"),
    "contrabn": sit_pct(without,"contrabn"),
    "arstmade": sit_pct(without,"arstmade")
    }
    print(all_sit_data)

    #Get use of Force Data for profile
    prof_force_data = {
    "pf_hands": sit_pct(stops,"pf_hands"),
    "pf_wall": sit_pct(stops,"pf_wall"),
    "pf_grnd": sit_pct(stops,"pf_grnd"),
    "pf_drwep": sit_pct(stops,"pf_drwep"),
    "pf_ptwep": sit_pct(stops,"pf_ptwep"),
    "pf_baton": sit_pct(stops,"pf_baton"),
    "pf_hcuff": sit_pct(stops,"pf_hcuff"),
    "pf_pepsp": sit_pct(stops,"pf_pepsp"),
    }
    print(prof_force_data)

    #Get use of Force Data for profile
    all_force_data = {
    "pf_hands": sit_pct(without,"pf_hands"),
    "pf_wall": sit_pct(without,"pf_wall"),
    "pf_grnd": sit_pct(without,"pf_grnd"),
    "pf_drwep": sit_pct(without,"pf_drwep"),
    "pf_ptwep": sit_pct(without,"pf_ptwep"),
    "pf_baton": sit_pct(without,"pf_baton"),
    "pf_hcuff": sit_pct(without,"pf_hcuff"),
    "pf_pepsp": sit_pct(without,"pf_pepsp"),
    }
    print(all_force_data)


    return render_template("more.html", psd=prof_sit_data, asd=all_sit_data,
        pfd=prof_force_data, afd=all_force_data)

"""

