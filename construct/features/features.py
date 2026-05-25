"""

DATUM: 25.05.2026
NAME: MARTIN
PURPOSE:
Here are all features collected. If creating an agent, those features are the columns of the Series that represents the agent.

"""

from enum import Enum

class Features(Enum):
    DATE_OF_BIRTH = 'DATE_OF_BIRTH'
    GENDER = 'GENDER'
    NAME = 'NAME'
    
    