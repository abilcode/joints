import numpy as np
import pandas as pd
import re

def type_of_other_floor_cleaner(data):
  # Lower the value
  data['type_of_other_floor'] = data['type_of_other_floor'].str.lower()

  # Change values
  data['type_of_other_floor'] = data['type_of_other_floor'].apply(lambda value: value.replace(r'reinforced cement concrete','rcc') if type(value) == str else value)
  data['type_of_other_floor'] = data['type_of_other_floor'].apply(lambda value: value.replace(r'reinforced brick concrete','rbc') if type(value) == str else value)

  # Fill NA dengan Modus
  mode = data['type_of_other_floor'].value_counts().index[0]
  data['type_of_other_floor'] = data['type_of_other_floor'].fillna(mode)

  # Get the first value
  data['type_of_other_floor'] = data['type_of_other_floor'].apply(lambda value: value.split()[0])
  data['type_of_other_floor'] = data['type_of_other_floor'].apply(lambda value: value.split('/')[0])
  data['type_of_other_floor'] = data['type_of_other_floor'].apply(lambda value: value.split('-')[0])

  # Return data
  return data