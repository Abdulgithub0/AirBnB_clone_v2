#!/usr/bin/python3
"""
define a view function to handle to user
request that involving db querying
"""

from flask import Flask, render_template
from models import storage

# create a class Flask instance
app = Flask(__name__, static_folder='static')


@app.teardown_appcontext
def close_session(error=None):
    """close the current open storage session for each request made"""
    storage.close()


# implement the logic for state listings
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters_view():
    """
        list or display all instances of State, City and Amenity
        objs with in either of the specify storage engine
    """
    from models.state import State
    from models.amenity import Amenity
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           States=states, Amenities=amenities)


if __name__ == "__main__":
    """launch flask app"""
    app.run(host="0.0.0.0", port=5000)
