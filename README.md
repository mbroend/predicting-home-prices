# Predicting Listing Prices of Homes in Denmark
This repo provides the code for:
* Gathering data by web-scraping a Danish real estate site
* Wrangling said data to a tidy format
* Using the data to create a machine learning model to predict listing prices

## Files
* Data Wrangling: Jupyter Notebook with the code to web scrape the Danish Real Estate company "home" for their listings and wrangling this data
* Data Analysis: Jupyter Notebook for analysing the listing data

## Verisons and libraries
Using the Anaconda distribution the following have been used:
* Python 3.7.3
* pandas 0.24.2
* request 2.21.0
* Beautiful soup (bs4) 4.7.1
* Sci-kit learn 
I haven't tested the code on any other version than the above.
Use at your own risk.

## Miscancellous
As always when using web scrapers, carefully think about the load you're putting on their servers. Consider if you can just use the data already gathered.