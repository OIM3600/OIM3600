from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
