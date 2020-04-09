from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    notes_file = open("notes.txt", "r", encoding = "UTF-8")
    notes_list = [row for row in notes_file]
    notes_file.close()
    return render_template('index.html', notes_list = notes_list)



@app.route("/hello/<string:user_name>")
def hello(user_name):
    user_name = user_name.capitalize()
    return render_template("hello.html", user_name = user_name)



@app.route("/add")
def add():
    return render_template("add.html")



@app.route("/add-note", methods = ["POST"])
def add_note():
    note = request.form.get("note")
    date = request.form.get("date")
    notes_file = open('notes.txt', 'a+', encoding = "UTF-8")
    notes_file.write(str(date) + " " + str(note) + "\n")
    notes_file.close()
    return render_template("qwerty.html")



@app.route("/table")
def table():
    notes_file = open("notes.txt", "r", encoding = "UTF-8")
    rows = [[row[:10], row[10:].strip()] for row in notes_file]
    notes_file.close()
    return render_template("table.html", rows = rows)