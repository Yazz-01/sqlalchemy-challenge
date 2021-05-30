# sqlalchemy-challenge
Project using SQLAlchemy and Flask

# Step 1 - Climate Analysis and Exploration

Using Python and SQLAlchemy I performed a basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

A jupyter notebook and hawaii.sqlite files were used to complete the climate analysis and data exploration. Bar charts and Area plot using matplotlib and seaborn were done to show the results.

#   Steps for the analysis:

1. Use SQLAlchemy create_engine to connect to sqlite database.


2. Use SQLAlchemy automap_base() to reflect tables into classes and save a reference to those classes called Station and Measurement.


3. Link Python to the database by creating an SQLAlchemy session.



# Precipitation Analysis


1. It starts by finding the most recent date in the data set. Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 

2. Select only the date and prcp values.

3. Loaded the query results into a Pandas DataFrame and set the index to the date column.

4. Sort the DataFrame values by date.

5. Plot the results using the DataFrame plot method.

6. Used Pandas to print the summary statistics for the precipitation data.

Fig. 1 is the Pandas summary statistics for the precipitation.

![last_months_of_precipitation](https://github.com/Yazz-01/sqlalchemy-challenge/blob/main/output_figures/last_months_of_precipitation_data.png)



# Station Analysis


1. Designed a query to calculate the total number of stations in the dataset.


2. Designed a query to find the most active stations (i.e. which stations have the most rows).


3. List the stations and observation counts in descending order.


4. The station id that has the highest number of observations.


5. Using the most active station id, calculate the lowest, highest, and average temperature. This step required a function such as func.min, func.max, func.avg, and func.count in queries.


6. Designed a query to retrieve the last 12 months of temperature observation data (TOBS).


7. Filtered by the station with the highest number of observations.


8. Query the last 12 months of temperature observation data for this station.


9. Plot the results as a histogram with bins=12.

![last_months_temp](https://github.com/Yazz-01/sqlalchemy-challenge/blob/main/output_figures/last_months_of_temp_data.png)



# Step 2 - Climate App

1. Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

2. Used Flask to create routes.


Routes
/
Home page.


3. List all routes that are available.

/api/v1.0/precipitation

Convert the query results to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.


/api/v1.0/stations

Return a JSON list of stations from the dataset.

/api/v1.0/tobs


4. Query the dates and temperature observations of the most active station for the last year of data.

Return a JSON list of temperature observations (TOBS) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

Calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

The start and the end date, calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.


  
#   Tricks

JOINED the station and measurement tables for some of the queries.

Used Flask jsonify to convert your API data into a valid JSON response object.



#   Other Recommended Analyses


Used temp_analysis_bonus_1.ipynb and temp_analysis_bonus_2 notebooks to perform challenging analysis.



# Temperature Analysis I


1.Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December? .Then I used pandas to perform this portion. Converted the date column format from string to datetime.

2. Set the date column as the DataFrame index

3. Drop the date column.

4.Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

5.Used the t-test to determine whether the difference in the means, if any, is statistically significant. 


# Temperature Analysis II


1. Since we are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.


2. The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.


3. Used the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").


4. Plot the min, avg, and max temperature from your previous query as a bar chart.

  ![Plot](https://github.com/Yazz-01/sqlalchemy-challenge/blob/main/output_figures/average_trip_temperature.png)


5. Used the average temperature as the bar height (y value).


6. Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).






# Daily Rainfall Average


1. Calculated the rainfall per weather station using the previous year's matching dates.

2. Sorted this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.




# Daily Temperature Normals


1. Calculated the daily normals for the duration of your trip. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.


2. Set the start and end date of the trip. Used the date to create a range of dates.


3. Striped off the year and save a list of strings in the format %m-%d.


4. Used the daily_normals function to calculate the normals for each date string and append the results to a list called normals.

5. Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

6. Use Pandas to plot an area plot (stacked=False) for the daily normals.
![Plot area](https://github.com/Yazz-01/sqlalchemy-challenge/blob/main/output_figures/trip_date_ranges_temp.png)
