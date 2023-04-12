import numpy as np
import pandas as pd
import re

def plinth_area_cleaner(data,fillna=False):
    # lower the words
  data['plinth_area (ft^2)'] = data['plinth_area (ft^2)'].str.lower()

  # replace 'More than 1000 ft^2' dengan '1001 ft^2'
  data['plinth_area (ft^2)'] = data['plinth_area (ft^2)'].replace({'more than 1000 ft^2':'1001 ft^2'})

  # replace ft^2 with ''
  data['plinth_area (ft^2)'] = data['plinth_area (ft^2)'].apply(lambda val: val.replace('ft^2','') if type(val) == str else val)

  # find the median
  non_null_plinth = data.dropna(subset = ['plinth_area (ft^2)'])
  non_null_plinth['plinth_area (ft^2)'] = non_null_plinth['plinth_area (ft^2)'].astype('float64')
  median_plinth_public = non_null_plinth.groupby(['public_place_type'])['plinth_area (ft^2)'].median().to_frame().reset_index()

  if fillna :
    # Buat kamus
    dict_plinth = dict(zip(median_plinth_public['public_place_type'], round(median_plinth_public['plinth_area (ft^2)'])))

    # Fill na
    data['plinth_area (ft^2)'] = data['plinth_area (ft^2)'].fillna(data['public_place_type'].map(dict_plinth))

  # Change to float type
  data['plinth_area (ft^2)'] = data['plinth_area (ft^2)'].astype('float16')

  # Return data
  return data
