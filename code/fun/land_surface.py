import numpy as np 
import pandas as pd
import re



def land_surface_condition_cleaner(data,fillna=False):
  if fillna :
    # Tentukan modus
    mode_land_surf = data['land_surface_condition'].value_counts().index[0]
    # Fill na
    data['land_surface_condition'] = data['land_surface_condition'].fillna(mode_land_surf)
  # Return data
  return data


