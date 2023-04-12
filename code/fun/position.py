import numpy as np 
import pandas as pd
import re


def position_cleaner(data,fillna=False):
  if fillna :
    # Fillna with Not Attached
    data['position'] = data['position'].fillna('Not attached')
  
  # Return data
  return data