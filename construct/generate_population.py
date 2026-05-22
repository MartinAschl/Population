"""

DATUM: 22.05.2026
NAME: MARTIN
SINN: Tools to add agents to population, change values of their features.

"""

import pandas as pd
import numpy as np

from database import values, features

class Population():
    
    def __init__(self, df: pd.DataFrame = None):
        
        if df is None:
            self.df = pd.DataFrame(columns=[feature.value for feature in features.Features])
        else:
            self.df = df.copy()
        
        

    def print(self):
        """
        simply returns a plot of first 10 rows of data.
        """
        print(self.df)
        
    def __add__(self, other):
        """ 
        Adds a person into the Population, but only assigns values to the initial features.
        """
        
        day = np.random.randint(0, 30)
        if day < 10:
            day = '0' + str(day) 
        month = np.random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        year = np.random.randint(1926, 2026)
        
        date_of_birth = f'{day}.{month}.{year}'
        gender = np.random.choice(a=values.GENDER).value
        
        agent = pd.Series({'DATE_OF_BIRTH': date_of_birth, 'GENDER': gender, 'ID': len(self.df)})
        self.df.loc[len(self.df)] = agent
        return self
        
Munich = Population()

for i in range(100):
    Munich += 1
    Munich.print()