"""
DATE: 25.05.2026
NAME: MARTIN
PURPOSE:
Generates value for the feature DATE_OF_BIRTH. Static feature which does not depend on other features
"""

import os
import sys

current_folder = os.path.dirname(os.path.abspath(__file__))
features_dir = os.path.dirname(current_folder)

if features_dir not in sys.path:
    sys.path.insert(0, features_dir)
    
from DATE_OF_BIRTH.date_of_birth_values import DATE_OF_BIRTH
import numpy as np

def _infer_date_of_birth():
    dof = np.random.choice(DATE_OF_BIRTH)
    return dof.value