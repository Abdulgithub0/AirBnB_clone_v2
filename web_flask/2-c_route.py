#!/usr/bin/python3
"""
a script that starts a Flask web application:
the web application is listening  on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display "HBNB"
    /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space)
"""
from flask import Flask

# create an instance of class Flask
app = Flask(__name__)


# bind a specific different url to the following views
@app.route("/c/<text>", strict_slashes=False)
def c_view():
    """display 'C' followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


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
