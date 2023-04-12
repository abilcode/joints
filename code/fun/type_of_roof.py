import numpy as np 
import pandas as pd
import re


def type_of_roof_cleaner(data,fillna):
  # Change values
  data['type_of_roof'] = data['type_of_roof'].apply(lambda value: value.replace(r'reinforced cement concrete','rcc') if type(value) == str else value)
  data['type_of_roof'] = data['type_of_roof'].apply(lambda value: value.replace(r'Reinforced Brick Slab','rb') if type(value) == str else value)
  data['type_of_roof'] = data['type_of_roof'].apply(lambda value: value.replace(r'Reinforced brick concrete','rbc') if type(value) == str else value)

  if fillna:  
    # Fill NA dengan Modus
    mode = data['type_of_roof'].value_counts().index[0]
    data['type_of_roof'] = data['type_of_roof'].fillna(mode)

  # Get the first value
  data['type_of_roof'] = data['type_of_roof'].apply(lambda x: x.split()[0] if type(x) == str else x)
  data['type_of_roof'] = data['type_of_roof'].apply(lambda x: x.split('/')[0] if type(x) == str else x)

  # Return data
  return data
