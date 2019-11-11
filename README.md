# Predicting Listing Prices of Real Estate in Denmark
Investing in real estate is probably the largest sum of money most individuals are going to spend at once in their lifetime, yet the decision to aquire a house or an appartment is often made rather quickly and on the basis of gut feeling, rather than data. 

I'm myself in a position where possibility of being a home owner is moving ever closer. But as a data guy I couldn't possibly conform to the norm and not base such a decision of the data.

The main questions I want to answer are:
* How much does location matter?
* Is it possible to predict listing prices based on characteristics of the home?
* If so, what features are most important?

This repo provides the code for:
* Gathering data by web-scraping a large Danish real estate site
* Wrangling said data to a tidy format
* Using the data to create a machine learning model to predict listing prices

## Files
* Data Wrangling: Jupyter Notebook with the code to web scrape the Danish Real Estate company "Home" for their listings and wrangling this data
* Data Analysis: Jupyter Notebook for analysing the listing data
* Data:
 * base_data: The result of scraping the entire home database
 * home_data: 
 * home_data_clean:
 * home_data_clean_final: 

## Verisons and libraries
Using the Anaconda distribution the following have been used:
* Python 3.7.3
* Pandas 0.24.2
* Request 2.21.0
* Beautiful soup (bs4) 4.7.1
* Scikit-learn  0.21.6
* Seaborn 0.9.0
* [Graphviz](https://www.graphviz.org/) 0.13.2 (note you need a standalone application as well)
I haven't tested the code on any other version than the above.

## Miscancellous
As always when using web scrapers, carefully think about the load you're putting on their servers. Consider if you can just use the data already gathered.