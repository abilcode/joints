import pandas as pd
import numpy as np
import re


def type_of_ground_floor_cleaner(data,fillna):
  # Lower the value
  data['type_of_ground_floor'] = data['type_of_ground_floor'].str.lower()

  # Change values
  data['type_of_ground_floor'] = data['type_of_ground_floor'].replace({'reinforced concrete':'rc'})

  # Fill NA dengan Modus
  if fillna:
    mode = data['type_of_ground_floor'].value_counts().index[0]
    data['type_of_ground_floor'] = data['type_of_ground_floor'].fillna(mode)

  # Get the first value
  data['type_of_ground_floor'] = data['type_of_ground_floor'].apply(lambda x: x.split()[0] if type(x) == str else x)
  data['type_of_ground_floor'] = data['type_of_ground_floor'].apply(lambda x: x.split('/')[0] if type(x) == str else x)
  data['type_of_ground_floor'] = data['type_of_ground_floor'].apply(lambda x: x.split('-')[0] if type(x) == str else x)

  # Return data
  return data