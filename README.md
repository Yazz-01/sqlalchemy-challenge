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

!last_months_temp](https://github.com/Yazz-01/sqlalchemy-challenge/blob/main/output_figures/last_months_of_temp_data.png)
