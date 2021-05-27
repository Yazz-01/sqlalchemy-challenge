# import Flask
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///titanic.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
# Create an app, being sure to pass __name__

app = Flask(__name__)

#################################################
# Flask Routes
#################################################


# 1. Home page route.
@app.route("/")
def welcome():
    print("Server received request from 'Home' page...")
    return (
        f"Welcome to my 'Home'page! API! <br/>"
    )


# 2. Index listing all routes that are available.
@app.route("/index")
def index():
    print("Server received request from 'Index' page...")
    return (
        f"AvailableRoutes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


# 3. Precipitation
@app.route("/api/v1.0/<precipitation>")
def show_precipitation(precipitation):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Results from Precipitation query
    # Starting from the most recent data point in the database. 
    twelve_months_precipt=session.query(Measurement.date, Measurement.prcp).\
                      filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()
    # Close session
    session.close()

    # Convert list of tuples into normal list
    all_months = list(np.rael(twelve_months_precipt))

return jsonify(all_months)




# 4. Stations
@app.route("/api/v1.0/<stations>")
def show_stations():




return jsonify()







# 5. Dates and temperature observations 
# of the most active station for the last year of data.
@app.route("/api/v1.0/<tobs>")
def show_stations(tobs):
    return jsonify()

# Return a JSON list of the minimum temperature, 
# the average temperature, and the max temperature 
# for a given start or start-end range.
@app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")
def show_stations():
    return jsonify()




if __name__== "__main__":
    app.run
    
