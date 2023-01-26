
## 03-Tidy

## Goals

* EDA with multivariable dataset (case study: USGS earthquake API)
* Processing and managing tidy/tabular data -- Pandas & Numpy
* Statistical visualization (with Seaborn and friends)

## Notebooks

* [02-numpy.ipynb](https://colab.research.google.com/drive/1ESDqb8LMcwTr8bjbdLDt_WACSzXBbP8z)
  * NumPy can do multidimensional arrays, among other amazing things!
* [02-pandas.ipynb](https://colab.research.google.com/drive/1KgNmykHXbI1VY_5ahmRPuOPfPdBbtBRV)
  * Grouping with Pandas
* [02-quakes-exercises.ipynb](https://colab.research.google.com/drive/1O91p2-FOs4VnmZmXFHbqyzq3q9xGIIxT)
  * histograms of earthquakes -- last month, all sizes
  * includes links to USGS API documentation and GeoJSON data model and data dictionary
* [03-central-limit-exercises.ipynb](https://colab.research.google.com/drive/1WWon45UuwOUAj6hwq-xSzUCazf_uIOOZ)
* [03-geopandas-exercises.ipynb](https://colab.research.google.com/drive/1Afw2dOJC_i8EreT2Fp8AtjO8cn1nGZ83)
* [03-observable-quakes-exercises.ipynb](https://colab.research.google.com/drive/1z_6ZDQ1zP5fARR1IFMMGSNbcC24xMz9s)
* polleverywhere: https://PollEv.com/pbogden
* [scratch notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG) -- shared

## Reading -- for next week

* [Interacting with databases](https://wesmckinney.com/book/accessing-data.html#io_databases) -- wesmkinney.com
  * The entire chapter is good: "Data Loading, Storage and File Formats" -- It introduces a variety of data formats.
  * It includes a discussion of JSON data (we used GeoJSON, a subset of JSON, when looking at earthquake data)
  * It also discusses web APIs (we get earthquake data from the USGS API)
  * The specific link above provides a brief introduction to SQL and relational databases.
  * Next week we'll be using sqlite3 -- McKinney provides example code.
  * If you're new to SQL and/or sqlite3, then try implementing the code in Colab -- experiment with it.
* [Comparison w/SQL](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html)
  * Pandas has a lot of built-in methods that perform the same functions as SQL.
  * This part of the pandas reference documentation makes a comparison.
* If you're entirely new to SQL, then try out the [SQL tutorial](https://www.w3schools.com/sql/) at w3schools.com


## hw1

* Due Sunday
* Available in Canvas
* Work independently -- submit URL in Canvas for the github repo created by github classroom

### Projects

* Mention them

### Central Limit Theorem

* [03-central-limit-exercises.ipyn](https://colab.research.google.com/drive/1WWon45UuwOUAj6hwq-xSzUCazf_uIOOZ)

### EDA of earthquakes

* Picking up from where we left off last week
* Last week, histograms exhibited two features of interest in the earthquakes from the previous month...
  * time dependent ditribution in earthquake (global aggregation) -- would expect a uniform distribution
  * magnitude has bi-modal distribution  -- would expect monotonic decrease in magnitude (skewed distribution)
  * wikipedia references...
    * [uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution)
    * [skewed distribution](https://en.wikipedia.org/wiki/Skewness) 
    * [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)

### EDA continued -- What's going on?

Adding maps, working with the API

* [03-geopandas-exercises.ipynb](https://colab.research.google.com/drive/1Afw2dOJC_i8EreT2Fp8AtjO8cn1nGZ83)
* [03-observable-quakes-exercises.ipynb](https://colab.research.google.com/drive/1z_6ZDQ1zP5fARR1IFMMGSNbcC24xMz9s)
