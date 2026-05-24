"""
DATE: 24.05.2026
NAME: MARTIN
PURPOSE:
Builds an agent by assigning all static features a value.
While some features are initialized, others built up on each other (f.e.: Name(Date of Birth, Gender))
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from construct.features import feature_functions

#print(feature_functions.infer_name('17.06.2003', 'FEMALE'))

class Agent():
    #CODE HERE
    pass

