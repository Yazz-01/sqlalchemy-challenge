# import Flask
from flask import Flask

# Create an app, being sure to pass __name__
app = Flask(__name__)

# 1. Home page route.
@app.route("/")
def home():
    print("Server received request from 'Home' page...")
    return "Welcome to my 'Home'page!"


# 2. Index listing all routes that are available.
@app.route("/about")
def index():
    print("Server received request from 'Index' page...")
    return "Available Routes:"


# 3. Precipitation
@app.route("/api/v1.0/precipitation")
def show_precipitation():
    return jsonify()

# 4. Stations
@app.route("/api/v1.0/stations")
def show_stations():
    return jsonify()


# 5. Dates and temperature observations 
# of the most active station for the last year of data.
@app.route("/api/v1.0/tobs")
def show_stations():
    return jsonify()

# Return a JSON list of the minimum temperature, 
# the average temperature, and the max temperature 
# for a given start or start-end range.
@app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")
def show_stations():
    return jsonify()





if __name__== "__main__":
    app.run
    
