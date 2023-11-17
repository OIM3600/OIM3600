from flask import Flask, redirect, render_template, request, url_for
from weather import get_temp

app = Flask(__name__)


@app.route("/")
def index():
    # return "<h1>Hello, World!</h1> <p>I am excited to learn Flask.</p>"
    return render_template("index.html")


@app.route("/hello")
def hello():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "guest"
    return render_template("hello.html", username=name)


@app.route("/ai")
def talk_ai():
    # form that allows user to enter text
    # After pressing "enter" key, send HTTP request to an endpoint of AI API
    # After getting response from the API
    # display the response
    pass


# @app.route("/weather")
# def weather():
#     return render_template("weather-form.html")


# @app.route("/temp")
# def temp():
#     if "city" in request.args:
#         city = request.args["city"]
#         city = city.replace(" ", "%20")
#     else:
#         city = "Wellesley"
#     temp = get_temp(city)
#     return f"The temperature of {city} is {temp}."


@app.get("/weather")
def weather_get():
    return render_template("weather-form1.html")


@app.post("/weather")
def weather_post():
    city = request.form.get("city")
    # temp = get_temp(city.replace(" ", "%20"))
    temp = 60
    # return f"The temperature of {city} is {temp}."
    return render_template("weather-result.html", city=city, temp=temp)


"""
404 Handling
"""


@app.errorhandler(404)
def page_not_found(e):
    return "Not found. 😭"


"""
Registration example
"""
students = {}
courses = ["Python", "Web", "Cybersecurity", "Mobile"]


@app.get("/register")
def register_get():
    return render_template("registration-form.html", courses=courses)


@app.post("/register")
def register_post():
    # validate the input
    name = request.form.get("name")
    course = request.form.get("course")
    if course not in courses:
        return f"Hello, hacker. You cannot register this course!"
    # register name and course to the dict
    students[name] = course
    return redirect("/students")


@app.route("/students")
def show_students():
    return render_template("students.html", students=students)


# Create another route("/double?number=3") so the response will be 6
@app.route("/double")
def double():
    if "number" in request.args:
        n = request.args["number"]
    else:
        n = 0
    res = float(n) * 2
    return f"{res}"


@app.route("/s")  # similar to Amazon search
def search():
    if "k" in request.args:
        k = request.args["k"]
    else:
        k = "the default search term"
    # Connecting to database to get matching products
    return f"You've found {k}!"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
