import numpy as np
import pandas as pd

from fun.floor_before_eq import floors_before_eq_cleaner as floor
from fun.plinth_area import plinth_area_cleaner as plinth
from fun.no_family_residing import no_family_residing_cleaner as fam
from fun.position import position_cleaner as pos




if __name__ == "__main__":
    data = pd.read_csv("../data/train.csv")