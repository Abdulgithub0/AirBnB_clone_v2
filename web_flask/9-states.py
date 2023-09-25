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
@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_view(id="not"):
    """
        /states
            list or display all instances of State obj with
            in either of the specify storage engine

        /states/<id>
            list or display all instances of State with respective cities
            obj based on search id parameter
    """
    from models.state import State
    states = storage.all(State)
    if (id):
        states = dict(filter(lambda x: x[1].id == id, states.items()))
        print(states)
    return render_template("9-states.html", States=states, search_id=id)



if __name__ == "__main__":
    """launch flask app"""
    app.run(host="0.0.0.0", port=5000)
