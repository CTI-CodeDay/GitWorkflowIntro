from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/2022")
def cohort_2022():
    return render_template('students_2022.html')

@app.route("/2023")
def cohort_2023():
    return render_template('students_2023.html')


@app.route("/2024")
def cohort_2024():
    return render_template('students_2024.html')


@app.route("/nat_uts")
def team_nat_uts():
    return render_template('teams/nat_uts.html')

@app.route("/sun_edm")
def team_sun_edm():
    return render_template('teams/sun_edm.html')

@app.route('/jaime_edgarh')
def team_jaime_edgarh():
    return render_template('teams/jaime_edgarh.html')

@app.route("/nathan_brian")
def team_nathan_brian():
    return render_template('teams/nathan_brian.html')

@app.route("/boba")
def team_boba():
    return render_template('teams/boba.html')

@app.route("/ian_brenden_elias")
def team_ian_brenden_elias():
    return render_template('teams/ian_brenden_elias.html')

@app.route("/edg_and_edg")
def team_edg_and_edg():
    return render_template('teams/edg_and_edg.html')

@app.route("/nt")
def team_nt():
    return render_template('teams/nt.html')

@app.route("/liu_tuan_dominic")
def team_liu_tuan_dominic():
    return render_template('teams/liu_tuan_dominic.html')

@app.route("/teamWork")
def team_june22():
    return render_template('teams/teamWork.html')

@app.route("/trav_con")
def team_trav_con():
    return render_template('teams/trav_con.html')

@app.route("/team_michael_rahul_magiber")
def team_michael_rahul_magiber():
    return render_template('teams/team_michael_rahul_magiber.html')
  
@app.route("/sleeper")
def team_sleeper():
    return render_template('teams/sleeper.html')

@app.route("/Team 10")
def team10():
    return render_template('teams/team10.html')

@app.route("/team_kn")
def team_kn():
    return render_template('teams/team_kn.html')

@app.route("/team_Di_Si_Se")
def team_Di_Si_Se():
    return render_template('teams/team_Di_Si_Se.html')

@app.route("/shengzhe")
def team_shengzhe():
    return render_template('teams/shengzhe.html')

@app.route("/james_david")
def team_james_david():
    return render_template('teams/james_david.html')

@app.route("/dong_zach_dar")
def team_dong_zach_dar():
    return render_template('teams/dong_zach_dar.html')

@app.route("/alison_rob_shawn")
def team_alison_rob_shawn():
    return render_template('teams/alison_rob_shawn.html')

@app.route("/nick_val")
def team_nick_val():
    return render_template('teams/nick_val.html')

@app.route("/luke_noah_maya")
def team_luke_noah_maya():
    return render_template('teams/luke_noah_maya.html')

@app.route("/sum_xiao_rios")
def team_sum_xiao_rios():
    return render_template('teams/sum_xiao_rios.html')