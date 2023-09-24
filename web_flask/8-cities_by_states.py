#!/usr/bin/python3
"""
define a view function to handle to user
request that involving db querying
"""

from flask import Flask, render_template
from models import storage

# create a class Flask instance
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error=None):
    """close the current open storage session for each request made"""
    storage.close()


# implement the logic for state listings
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_view():
    """
        list or display all instances of City obj with
        corresponding State obj in either of the specify storage engine
    """
    from models.state import State
    states = storage.all(State)
    return render_template("8-cities_by_states.html", States=states)


if __name__ == "__main__":
    """launch flask app"""
    app.run(host="0.0.0.0", port=5000)
