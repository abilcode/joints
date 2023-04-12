import pandas as pd
import numpy as np
import re


def legal_ownership_status_cleaner(data,fillna):
  if fillna:
    # Fillna
    data['legal_ownership_status'] = data['legal_ownership_status'].fillna('Unknown')

  # Replace Values
  data['legal_ownership_status'] = data['legal_ownership_status'].replace({'Private Use':'Private',
                                                                           'Prvt':'Private',
                                                                           'Privste':'Private',
                                                                           'Public Use':'Public',
                                                                           'Public Space':'Public',
                                                                           'Institutionals':'Institutional',
                                                                           'Institutional Use':'Institutional',
                                                                           'Unspecified':'Other'})
  # Return data
  return data