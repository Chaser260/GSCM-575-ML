import pandas as pd

# import .csv file
# countries = pd.read_csv('https://raw.githubusercontent.com/AlexTheAnalyst/PandasYouTubeSeries/main/countries%20of%20the%20world.csv')
# countries

# import txt file using read_table
# countries = pd.read_table('https://raw.githubusercontent.com/AlexTheAnalyst/PandasYouTubeSeries/main/countries%20of%20the%20world.txt')
# countries

# import .json file using read_json
json = pd.read_json('https://raw.githubusercontent.com/AlexTheAnalyst/PandasYouTubeSeries/main/json_sample.json')
json

pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 18)
pd.set_option('display.width', None)
countries

# View data frame information (# of entries, columns, non-null count, datatype)
countries.info()

# view number of (rows, columns)
countries.shape

# head gives first 5 rows by default, or specify the number of rows you want to view.
countries.head()

# tail gives last 5 rows, or specify the number of rows you want to view.
countries.tail()

countries.loc[200]

# View the first 5 rows of the Country column
countries["Country"].head()

import matplotlib.pyplot as plt
import numpy as np

df[df['Rank'] < 10]