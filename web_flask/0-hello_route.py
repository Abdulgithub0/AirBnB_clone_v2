#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask

# create an instance of class Flask
app = Flask(__name__)


# bind a specific url to the view hello function
@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    # launch the hello_route app
    app.run(host=0, port=5000)
