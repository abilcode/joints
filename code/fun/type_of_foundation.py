import pandas as pd
import numpy as np
import re

def type_of_foundation_cleaner(data,fillna):
  # Replace values
  data['type_of_foundation'] = data['type_of_foundation'].replace({'Others':'Other',
                                                                   'Reinforced Concrete':'RC'})
  if fillna:
    # Dapatkan modus
    mode = data['type_of_foundation'].value_counts().index[0]

    # Fill na
    data['type_of_foundation'] = data['type_of_foundation'].fillna(mode)

  # Get the first word
  data['type_of_foundation'] = data['type_of_foundation'].apply(lambda x: str(x).split()[0])
  data['type_of_foundation'] = data['type_of_foundation'].apply(lambda x: str(x).split('/')[0])

  # Return data
  return data