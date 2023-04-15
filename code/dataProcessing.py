
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline

from fun.floor_before_eq import floors_before_eq_cleaner as floor
from fun.plinth_area import plinth_area_cleaner as plinth
from fun.no_family_residing import no_family_residing_cleaner as fam
from fun.position import position_cleaner as pos
from fun.land_surface import land_surface_condition_cleaner as land
from fun.type_of_foundation import type_of_foundation_cleaner as fond
from fun.type_of_roof import type_of_roof_cleaner as roof
from fun.type_of_floor import type_of_other_floor_cleaner as other_floor
from fun.type_of_ground import type_of_ground_floor_cleaner as ground 
from fun.legal_ownership import legal_ownership_status_cleaner as legal

def preprocessing(data):
    
    tmp = data.copy()
    tmp = floor(tmp,False)
    tmp = plinth(tmp,False)
    tmp = fam(tmp,False)
    tmp = pos(tmp,False)
    tmp = land(tmp,False)
    tmp = fond(tmp,False)
    tmp = roof(tmp,False)
    tmp = other_floor(tmp,False)
    tmp = legal(tmp,False)
    tmp = ground(tmp,False)
    return tmp

def drop(data):
    tmp = data.copy()
    return tmp

if __name__ == "__main__":
    train = pd.read_csv("../data/train.csv")
    train_t = preprocessing(train)
    test = pd.read_csv("../data/test.csv")
    test_t = preprocessing(test)
    print(train.isna().sum(),train_t.isna().sum(),sep='\n'*3)
    train_t.to_csv("../data/preprocess/train_2.csv")
    test_t.to_csv("../data/preprocess/test_2.csv")
