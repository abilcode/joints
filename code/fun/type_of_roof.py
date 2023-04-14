
import numpy as np 
import pandas as pd
import re


def type_of_roof_cleaner(data,fillna):
  # Change values
   # Lower values
  data['type_of_roof'] = data['type_of_roof'].str.lower()

  # Change values
  data['type_of_roof'] = data['type_of_roof'].apply(lambda value: value.replace(r'reinforced cement concrete','rcc') if type(value) == str else value)
  data['type_of_roof'] = data['type_of_roof'].apply(lambda value: value.replace(r'reinforced brick slab','rb') if type(value) == str else value)
  data['type_of_roof'] = data['type_of_roof'].apply(lambda value: value.replace(r'reinforced brick concrete','rbc') if type(value) == str else value)
  data['type_of_roof'] = data['type_of_roof'].replace({'bamboo/timber-light roof':'bamboo/timber light roof',
                                                       'bamboo or timber light roof': 'bamboo/timber light roof',
                                                       'bamboo/timber-heavy roof':'bamboo/timber heavy roof',
                                                       'bamboo or timber heavy roof':'bamboo/timber heavy roof',
                                                       'rcc/rb/rbc':'rb/rcc/rbc',
                                                       'rbc/rcc/rbc':'rb/rcc/rbc'})

  if fillna:  
    # Fill NA dengan Modus
    mode = data['type_of_roof'].value_counts().index[0]
    data['type_of_roof'] = data['type_of_roof'].fillna(mode)

  # # Get the first value
  # data['type_of_roof'] = data['type_of_roof'].apply(lambda x: x.split()[0] if type(x) == str else x)
  # data['type_of_roof'] = data['type_of_roof'].apply(lambda x: x.split('/')[0] if type(x) == str else x)

  # Return data
  return data
