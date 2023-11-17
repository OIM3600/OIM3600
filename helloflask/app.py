from flask import Flask, render_template, request

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
