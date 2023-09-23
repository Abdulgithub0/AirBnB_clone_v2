#!/usr/bin/python3
"""
a script that starts a Flask web application:
the web application is listening  on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display "HBNB"
    /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space)
    /python/<text>: display “Python ”, followed by the value of
        the text variable
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask, render_template
from markupsafe import escape

# create an instance of class Flask
app = Flask(__name__)


# bind a specific different url to the following views
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_view(n):
    return render_template("5-number.html", number=n)


@app.route("/number/<int:n>", strict_slashes=False)
def number_view(n):
    """display 'n is a number'"""
    if n and type(n) is int:
        return f"{n} is a number"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_view(text: str = "is cool"):
    """Display 'Python' followed by the value of the text variable"""
    return "Python {}".format(escape(text).replace('_', ' '))


@app.route("/c/<text>", strict_slashes=False)
def c_view(text):
    """display 'C' followed by the value of the text variable"""
    return "C {}".format(escape(text).replace("_", " "))


@app.route("/hbnb", strict_slashes=False)
def hbnb_view():
    """Return an html page with body containing HBNB"""
    return "HBNB"


@app.route("/", strict_slashes=False)
def default_view():
    """Return an html page with body containing hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # launch the hello_route app
    app.run(host=0)
