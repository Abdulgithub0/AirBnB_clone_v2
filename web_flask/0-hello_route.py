#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask

# create an instance of class Flask
hello_route = Flask(__name__)


# bind a specific url to the hello function
@hello_route.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    # launch the hello_route app
    hello_route.run(host=0, port=5000)
