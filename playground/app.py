from flask import Flask, render_template

app=Flask(__name__)

one=("Raymond", 84, "Junior")
two=("John",68, "Senior")
three=("Pat", 85, "Sophomore")
four=("Sam",79, "Junior")
five=("Erin",55,"Senior")
six=("Alex", 67,"Freshman")
seven=("Paul",55,"Senior")

class_roster=[one,two,three,four,five,six,seven];

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", name=name)

@app.route("/roster/<int:gradeview>")
def roster(gradeview):
    return render_template("roster.html",gradeview=gradeview, class_roster=class_roster)
