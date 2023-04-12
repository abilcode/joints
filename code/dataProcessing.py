import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline

from fun.floor_before_eq import floors_before_eq_cleaner as floor
from fun.plinth_area import plinth_area_cleaner as plinth
from fun.no_family_residing import no_family_residing_cleaner as fam
from fun.position import position_cleaner as pos
from fun.land_surface import land_surface_condition_cleaner as land
from fun.type_of_foundation import type_of_foundation_cleaner as fond

def processing(data):
    
    data = floor(data,True)
    data = plinth(data,True)
    data = fam(data,False)
    data = pos(data,True)
    
    return data
    


if __name__ == "__main__":
    train = pd.read_csv("../data/train.csv")
    train_t = train.copy()
    train_t = processing(train_t)
    print(train.isna().sum(),train_t.isna().sum())
    