from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/registered", methods=["POST"])
def register():
    name = request.form.get("name")
    classid = request.form.get("classid")
    if not name or not classid:
        return render_template("failure.html")
    else:
        file = open("registrants.csv", "a", newline='')
        writer = csv.writer(file)
        writer.writerow((name, classid))
        file.close()
        return render_template("success.html")

@app.route("/registrants")
def registrants():
    with open("registrants.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template("registrants.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)