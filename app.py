import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt
import csv
import json
import numpy as np
import pandas as pd
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table- Assigning the class to a variable Station and Measurement
Station= Base.classes.station
Measurement= Base.classes.measurement
print(Base.classes.keys())

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
        f"AvailableRoutes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )





# 3. Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Results from Precipitation query
    # Starting from the most recent data point in the database. 
    twelve_months_precipt=session.query(Measurement.date, Measurement.prcp).\
                      filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()
 
    # Convert list of tuples into normal list
    all_months = list(np.ravel(twelve_months_precipt))

    return jsonify(all_months)




# 4. Stations
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Using the most active station id
    # Query the last 12 months of temperature observation data for this station
    # Use the session to query Measurement table and display the first 15 trade volumes
    for row in session.query(Measurement.date, Measurement.tobs).limit(15).all():
        print(row)
    
    
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(active_month))

    return jsonify(all_stations)




# 5. Dates and temperature observations 
# of the most active station for the last year of data.
@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
 
#     ## Combine the data into a single dataset
    active_month= session.query(Measurement.tobs).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()
#   
    # Convert list of tuples into normal list
    all_temps = list(np.ravel(active_month))

#     # Convert list of tuples into normal list
#    # all_stations = list(np.ravel(active_month))
    
    return jsonify(all_temps)




@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def averages_stats(start=None, end=None):
    
    session = Session(engine)
    
    diff_temp= [func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]

    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    if not end:
        diff_tobs = session.query(*diff_temp).filter(Measurement.date >= start).all()
        all_tobs = list(np.ravel(diff_tobs))
        
        return jsonify(all_tobs)
    
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    diff_tobs = session.query(*diff_temp).\
    filter(Measurement.date.between(start, end)).all()

     
    all_tobs = list(np.ravel(diff_tobs))
    return jsonify(all_tobs)



if __name__== "__main__":
    app.run()
    
