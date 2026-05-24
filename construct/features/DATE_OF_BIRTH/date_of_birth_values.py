""" 

DATE: 24.05.2026
NAME: MARTIN
PURPOSE: DATE_OF_BIRTH contains all possible birthdays (30.02.XXXX is possible as well) in the following way:
    _DAY_MONTH_YEAR = 'DAY.MONTH.YEAR'

"""


from enum import Enum

DATE_OF_BIRTH_dict = {}

START_YEAR, END_YEAR = 1926, 2026 

for i in range(1926, 2027):
    for j in range(1, 13):
        for k in range(1, 31):
            ordinate = f'{k:02d}.{j:02d}.{i}'
            abscissa = f'_{k:02d}_{j:02d}_{i}'
            DATE_OF_BIRTH_dict[abscissa] = ordinate            

DATE_OF_BIRTH = Enum('DATE_OF_BIRTH', DATE_OF_BIRTH_dict)



    
