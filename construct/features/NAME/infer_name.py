""" 
DATE: 24.05.2026 
NAME: MARTIN
PURPOSE: 
Name is computed with respect to DATE_OF_BIRTH and GENDER. Feature DATE_OF_BIRTH is static and inferred.
"""

import os
import sys

file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(file_path)
features_dir = os.path.dirname(current_dir)

if features_dir not in sys.path:
    sys.path.insert(0, features_dir)

from DATE_OF_BIRTH.date_of_birth_values import START_YEAR, END_YEAR
from GENDER.gender_values import GENDER
from construct.features.NAME.name_values import NAME, NAME_FEMALE, NAME_MALE

import pandas as pd
import numpy as np

def _infer_name(x1: str, x2: str) -> str:
    """ 
    INPUT: DATE_OF_BIRTH: "DATE.MONTH.YEAR"; GENDER: "MALE"/"FEMALE"
    OUTPUT: inferred NAME.
    """
    
    # Return Martin FOR x1 = 17.06 and x2 = Male
    day_month = f'{x1.split('.', 1)[0]}' + '.' + f'{x1.split('.', 2)[1]}' 
    
    if day_month == '17.06' and x2 == f'{GENDER['MALE'].value}':
        return 'MARTIN'
    
    #1. GENERATES THE NAME TABLE
    
    rows = []
    
    for year in range(START_YEAR, END_YEAR):
        for gender in GENDER:
            for name in NAME:
                if gender == GENDER['MALE'] and name.value in NAME_FEMALE:
                    continue
                elif gender == GENDER['FEMALE'] and name.value in NAME_MALE:
                    continue
                else: 
                    rows.append({'YEAR': year,
                                'GENDER': gender.value,
                                'NAME': name.value,
                                'freq': np.random.random()})
               
    rows = pd.DataFrame(rows)
    
    #2. SELECTS POSSIBLE NAMES AND THEIR RESPECTIVE FREQUENCIES
    birth_year = int(x1.split(".", 2)[2])
    gender = x2
    
    possible = rows[rows['YEAR'] == birth_year]
    possible = possible[possible['GENDER'] == gender]
    
    #3. NORMALIZE THE FREQUENCY
    
    Normalizer = possible['freq'].sum()
    possible['freq'] = possible['freq']/Normalizer
    possible = possible.reset_index(drop=True)
    
    #4. SELECT SUCCESSOR
    
    random_choice = np.random.random()
    count = possible.iloc[0]['freq']
    for i in range(len(possible)):
        if random_choice < count:
            return possible.iloc[i]['NAME']
        else:
            if i + 1 < len(possible):
                count += possible.iloc[i + 1]['freq']
    
    return possible.iloc[-1]['NAME']


