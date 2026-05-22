"""

DATUM: 22.05.2026
NAME: MARTIN
SINN: Um features aufeinander aufzubauen wurde eine Funktion gebaut, die gegebene Series transformiert.

"""

import numpy as np
import pandas as pd

feature1 = pd.Series({'1': 100, '2': 250, '3': 430})

def add_gaussian_white_noise(feature_old: pd.Series, mean: float, std: float) -> pd.Series:
    """
    new_signal = old_signal + noise (noise ~ N(mean, std))
    """
    
    if std >= 0:
        raise ValueError('[ERROR] STD MUST BE > 0')
    
    feature_new = feature_old + np.random.normal(mean, std, len(feature_old))
    return feature_new



