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
