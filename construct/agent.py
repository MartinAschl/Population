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

from construct.features import feature_functions as FF
from construct.features import features as F

import pandas as pd

class Agent():
    
    def __init__(self, **kwargs):
        for feature in F.Features:
            setattr(self, feature.value, None)
    
    @property    
    def df(self):    
        return pd.DataFrame(data=[self.__dict__])
    
    def show(self) -> None:
        """
        prints the agents as a DataFrame, returns nothing.
        """
        print(self.df)
        
    def fill(self) -> pd.DataFrame:
        """
        Assigns a value to all features that currently have value 'None'.
        """
        return self.df 
    
    def assign_date_of_birth(self) -> pd.DataFrame:
        self.DATE_OF_BIRTH = FF.infer_date_of_birth()
        return self.df
    
    def assign_gender(self) -> pd.DataFrame:
        self.GENDER = FF.infer_gender()
        return self.df
    
    def assign_name(self) -> pd.DataFrame:
        if self.DATE_OF_BIRTH == None or self.GENDER == None:
            raise ValueError('[ERROR] To infer a name, the date_of_birth and gender must be assigned first!')
        self.NAME = FF.infer_name(self.DATE_OF_BIRTH, self.GENDER)
        return self.df
    
Agent1 = Agent()
Agent1.show()
Agent1.assign_date_of_birth()
Agent1.assign_gender()
Agent1.assign_name()
Agent1.show()

    
    


