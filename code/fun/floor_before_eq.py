import numpy as np
import pandas as pd
import re


def floors_before_eq_cleaner(data,fillna=False):
  # Lower all text
  data['floors_before_eq (total)'] = data['floors_before_eq (total)'].str.lower()
  # Make dictionary
  dict_num = {'one': '1',
              'two': '2',
              'three': '3',
              'four':'4',
              'five':'5',
              'first':'1',
              'second':'2',
              'third':'3',
              'fourth':'4',
              'fifth': '5',}
  # Replace the number word
  for num in dict_num.keys():
    data['floors_before_eq (total)'] = data['floors_before_eq (total)'].apply(lambda value: value.replace(num, dict_num.get(num)) if type(value) == str else value)
  
  # Remove all words
  data['floors_before_eq (total)'] = data['floors_before_eq (total)'].apply(lambda value: re.findall('\d+', value)[0] if type(value) == str else value)

  if fillna:
    # Find the mode
    mode = data['floors_before_eq (total)'].value_counts().index[0]

    # Fill the NA
    data['floors_before_eq (total)'] = data['floors_before_eq (total)'].fillna(mode)

  # Set to float64
  data['floors_before_eq (total)'] = data['floors_before_eq (total)'].astype('float16')

  return data