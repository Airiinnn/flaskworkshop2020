from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/registered", methods=["POST"])
def registered():
    name = request.form.get("name")
    classid = request.form.get("classid")
    if not name or not classid:
        return render_template("failure.html")
    students.append("{} from {}".format(name, classid))
    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)