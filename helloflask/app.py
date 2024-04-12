from flask import Flask, redirect, request, render_template
from weather import get_weather_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name is not None:
        return f"Hello, {name}!"
    return "Hello, World!"


@app.route("/greet")
def greet():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "world"
    return render_template("hello.html", username=name)


@app.route("/search")
def get_greet():
    return render_template("hello-form.html")


@app.route("/get_temp")
def get_temp():
    return render_template("temp-form.html")


@app.route("/temp")
def show_temp():
    if "city" in request.args:
        city = request.args["city"]
        temp = get_weather_data(city)
        return render_template("temp-result.html", city=city, temp=temp)
    else:
        return "You need to provide a city name."


"""
Handling 404
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


"""
Registration Example
"""

STUDENTS = {}  # 'Alex': 'Finance', 'Gahyeon': 'Python', ...
COURSES = ['CS', 'Web', 'Python', 'Blockchain']

@app.get("/register")
def get_register():
    return render_template("register-form.html", courses=COURSES)


@app.post("/register")
def post_register():
    """
    Register course for a student
    """
    # Validate
    name = request.form.get("name")
    course = request.form.get("course")
    if course not in COURSES:
        return 'Get out of here, hacker!'
    STUDENTS[name] = course  # Real registration
    return redirect("/students")


@app.route("/students")
def show_students():
    return render_template("students.html", students=STUDENTS)


if __name__ == "__main__":
    app.run(debug=True)
