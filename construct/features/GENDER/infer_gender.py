"""
DATE: 25.05.2026
NAME: MARTIN
PURPOSE:
returns the feature gender. Probabilities for MALE/FEMALE can be adjusted in gender_values.py. feature is static and not inferred from other features.
"""

import os
import sys

file_path = os.path.dirname(os.path.abspath(__file__))
features_dir = os.path.dirname(file_path)

if features_dir not in sys.path:
    sys.path.insert(0, features_dir)

from GENDER.gender_values import GENDER, GENDER_PROB
import numpy as np

def _infer_gender():
    if np.random.random() < GENDER_PROB.FEMALE.value:
        return GENDER['FEMALE'].value
    else:
        return GENDER['MALE'].value   