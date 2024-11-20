import datetime
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from bitcoin import get_bitcoin_price
import weather

app = FastAPI()
templates = Jinja2Templates("templates")


# @app.get("/")
# async def root():
#     return {"message": "Hello World", "data": [1, 2, 3, 4]}


# @app.get("/", response_class=HTMLResponse)
# def homepage():
#     html_content = """
#     <html>
#     <head>
#         <title>Hello</title>
#     </head>
#     <body>
#         <h1>Hello, world!</h1>
#         <p>I am excited to learn FastAPI to create web applications.</p>
#     </body>
#     </html>
#     """
#     return html_content


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


@app.get("/hello", response_class=HTMLResponse)
@app.get("/hello/{name}", response_class=HTMLResponse)
def hello(request: Request, name="guest"):
    return templates.TemplateResponse(
        "hello.html",
        {
            "request": request,
            "username": name.capitalize(),
        },
    )


# Define another function, say double, that will implement the route /double/<number> and return the result of double the number


@app.get("/double", response_class=HTMLResponse)
@app.get("/double/{number}", response_class=HTMLResponse)
def hello(request: Request, number=0):
    result = float(number) * 2
    return f"<h1>Result = {result}</h1>"


@app.get("/hi", response_class=HTMLResponse)
def say_hi():
    return "Hi, guest"


@app.get("/search", response_class=HTMLResponse)
def search(q="python"):
    """Search for a term, just like google"""
    return f"We've found these results for the term {q}:"


@app.get("/ai", response_class=HTMLResponse)
def talk_ai(q="python"):
    """Search for a term, just like google"""
    return f"blah bla bla"


"""
Custom 404 page
"""


@app.exception_handler(404)
def custom_404(request, e):
    return HTMLResponse("Not found! 😭")


"""
Weather Example
"""

# # API example, JSON is returned
# @app.get("/temp")
# def temp(city="Wellesley"):
#     """Get temperature for a given city"""
#     result = weather.get_temp(city)
#     return {"city": city, "temp": result}


# Web example, HTML is returned
@app.get("/temp", response_class=HTMLResponse)
def temp(request: Request, city=None):
    """Get temperature for a given city"""
    if city is None:
        city = "Wellesley"
    result = weather.get_temp(city)
    return templates.TemplateResponse(
        "weather-result.html",
        {
            "request": request,
            "city": city.capitalize(),
            "temperature": result,
        },
    )


"""
Weather example via Form
"""


@app.get("/weather", response_class=HTMLResponse)
def get_weather(request: Request):
    return templates.TemplateResponse("weather-form.html", {"request": request})


@app.post("/weather", response_class=HTMLResponse)
async def post_weather(request: Request):
    form = await request.form()
    city = form.get("city")
    city = city.replace(" ", "%20")
    result = weather.get_temp(city)
    return templates.TemplateResponse(
        "weather-result.html",
        {
            "request": request,
            "city": city.capitalize(),
            "temperature": result,
        },
    )


"""
Bitcoin Example
"""

# "/bitcoin" -> form, where users can buy
# "/bitcoin/transactions" -> show all the transactions

bitcoins = {
    "transactions": [],
    "total_cost": 0,
    # "total_cost_comma": "0",
}


# def save_bitcoins():
#     with open("data/bitcoins.json", "w") as file:
#         json.dump(bitcoins, file)


# def load_bitcoins():
#     global bitcoins
#     with open("data/bitcoins.json", "r") as file:
#         bitcoins = json.load(file)


# load_bitcoins()


@app.get("/bitcoin", response_class=HTMLResponse)
def show_buy_bitcoin_form(request: Request):
    return templates.TemplateResponse("buy-bitcoin.html", {"request": request})


@app.post("/bitcoin", response_class=HTMLResponse)
async def buy_bitcoin(request: Request):
    """Process the form submission to fake-buy bitcoin"""
    form = await request.form()
    quant = form.get("quantity")
    quant = float(quant)
    price = get_bitcoin_price()
    total = price * quant
    total = round(total, 2)
    bitcoins["transactions"].append(
        {
            "quantity": quant,
            "price": price,
            "total": total,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    bitcoins["total_cost"] += total
    # bitcoins['total_cost_comma'] = f'{str(total):,}'

    # save_bitcoins()

    # return templates.TemplateResponse(
    #     "bitcoin.html", {"request": request, "bitcoins": bitcoins}
    # )
    return RedirectResponse(url="/bitcoin/transactions", status_code=303)


@app.get("/bitcoin/transactions", response_class=HTMLResponse)
def show_all_bitcoin_transactions(request: Request):
    return templates.TemplateResponse(
        "bitcoin.html",
        {
            "request": request,
            "bitcoins": bitcoins,
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
