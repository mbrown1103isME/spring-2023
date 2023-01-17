
## 02-DataViz

## Goals

* Introduce data viz in python
* Manipulation of data types
* (Re)Introduce NumPy and Pandas

## Links

* repo for class notes: https://github.com/ds5110/spring-2023
* polleverywhere: https://PollEv.com/pbogden
* [scratch notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG) -- shared

## Reading -- for next week

* [Data structures accepted by Seaborn](https://seaborn.pydata.org/tutorial/data_structure.html)
  * describes "tidy" data -- long-form and wide-form
* VanderPlas
  * [03.06-Concat-and-Append.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.06-Concat-And-Append.ipynb)
  * [03.07-Merge-and-Join.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.07-Merge-and-Join.ipynb)
* McKinney
  * [8 Data Wrangling: Join, Combine and Reshape](https://wesmckinney.com/book/data-wrangling.html)
  * [10 Data Aggregation & Group Operations](https://wesmckinney.com/book/data-aggregation.html)

## Resources -- overview

* McKinney, 3rd Edition
  * [Chapter 3: Built-in data structures, functions, and files](https://wesmckinney.com/book/python-builtin.html)
  * [Chapter 4: Numpy basics: arrays and vectorized computation](https://wesmckinney.com/book/numpy-basics.html)
  * [Chapter 5: Getting started with pandas](https://wesmckinney.com/book/pandas-basics.html)
    * Series (1-D)
    * DataFrames (2-D)
  * [Chapter 9: Plotting and visualization](https://wesmckinney.com/book/plotting-and-visualization.html)
    * matlotlib
    * seaborn
* [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) (2016) by Jake VanderPlas
  * Chapter 2 -- Introduction to Numpy
  * Chapter 3 -- Introduction to Pandas
  * Chapter 4 -- Introduction to Matplotlib
* API reference docs
  * [numpy](https://numpy.org/doc/stable/reference/index.html)
  * [pandas](https://pandas.pydata.org/docs/reference/index.html#api)
  * [matplotlib](https://matplotlib.org/stable/api/pyplot_summary.html)
    * [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
  * [seaborn](https://seaborn.pydata.org/api.html)
* How to search the reference docs
  * stackoverflow can be a great path to the documentation -- if used wisely!
  * google your error message (colab offers a search of stackoverflow for you)
  * it helps if you know [How to ask a question](https://stackoverflow.com/help/how-to-ask) -- stackoverflow.com

## Conventions

Standard practice:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Bad idea:
```
from numpy import *
```

## In-class exercise

Reproduce the three graphs in Figure 1.1 of ISL

* [02-wage-exercises](https://colab.research.google.com/drive/1_u_25hpoblox_Fm6ghHTcyDRRuMROELY)

## Git intro

The format for assignment submissions.

## Quakes

* [02-quakes-exercises.ipynb](https://colab.research.google.com/drive/1O91p2-FOs4VnmZmXFHbqyzq3q9xGIIxT)
