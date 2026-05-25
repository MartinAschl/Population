from enum import Enum

class GENDER(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    
class GENDER_PROB(Enum):
    _female_prob = 0.5
    MALE = 1 - _female_prob
    FEMALE = _female_prob