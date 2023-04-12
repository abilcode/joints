import numpy as np
import pandas as pd
import re



def no_family_residing_cleaner(data):
  # Replace NaN with None
  data['no_family_residing'] = data['no_family_residing'].fillna('None')

  # Change None into '0'
  data['no_family_residing'] = data['no_family_residing'].replace({'None':'0'})

  # Change type to float
  data['no_family_residing'] = data['no_family_residing'].astype('float16')

  # Return data
  return data