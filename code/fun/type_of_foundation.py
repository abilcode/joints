import pandas as pd
import numpy as np
import re

def type_of_foundation_cleaner(data,fillna):
  # Replace values
  
  data['type_of_foundation'] = data['type_of_foundation'].str.lower()
  data['type_of_foundation'] = data['type_of_foundation'].replace({'others':'other',
                                                                   'reinforced concrete':'rc',
                                                                   'bamboo or timber':'bamboo/timber',
                                                                   'clay sand mixed mortar-stone/brick':'clay mortar-stone/brick',
                                                                   'cement-stone or cement-brick':'cement-stone/brick'})
  if fillna:
    # Dapatkan modus
    mode = data['type_of_foundation'].value_counts().index[0]

    # Fill na
    data['type_of_foundation'] = data['type_of_foundation'].fillna(mode)

  # # Get the first word
  # data['type_of_foundation'] = data['type_of_foundation'].apply(lambda x: x.split()[0] if type(x) == str else x)
  # data['type_of_foundation'] = data['type_of_foundation'].apply(lambda x: x.split('/')[0] if type(x) == str else x )

  # Return data
  return data