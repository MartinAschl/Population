"""

DATUM: 22.05.2026
NAME: MARTIN
SINN: All values that a certain feature can have.

"""

from enum import Enum

class GENDER(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    
class OCCUPATION(Enum):
    PLUMBER = 'PLUMBER'
    ELECTRICIAN = 'ELECTRICIAN'
    DOCTOR = 'DOCTOR'
    INVESTMENT_BANKER = 'INVESTMENT_BANKER'
    PILOT = 'PILOT'
    ATTORNEY = 'ATTORNEY'
    SCIENTIST = 'SCIENTIST'
    ENGINEER = 'ENGINEER'
    SOFTWARE_ENGINEER = 'SOFTWARE_ENGINEER'
    TEACHER = 'TEACHER'
    NURSE = 'NURSE'
    CONSULTANT = 'CONSULTANT'
    CRAFTSMAN = 'CRAFTSMAN'

class NAME_MALE(Enum):
    PAUL = 'PAUL'
    ALEX = 'ALEX'
    JOE = 'JOE'
    NOAH = 'NOAH'
    MATTEO = 'MATTEO'
    HENRY = 'HENRY'
    ELIAS = 'ELIAS'
    THEO = 'THEO'
    LIAM = 'LIAM'
    OSKAR = 'OSKAR'
    FELIX = 'FELIX'
    EMIL = 'EMIL'
    MILAN = 'MILAN'
    MARTIN = 'MARTIN'
    KORDT = 'KORDT'
    VASI = 'VASI'
    KORNELIUS = 'KORNELIUS'
    
class NAME_FEMALE(Enum):
    LISA = 'LISA'
    ANNA = 'ANNA'
    SOPHIA = 'SOPHIA'
    EMMA = 'EMMA'
    EMILIA = 'EMILIA'
    MIA = 'MIA'
    HANNAH = 'HANNAH'
    IDA = 'IDA'
    MILA = 'MILA'
    EMILY = 'EMILY'
    LIA = 'LIA'
    MALIA = 'MALIA'
    
class GOAL(Enum):
    RICH = 'MONEY'
    POWER = 'POWER'
    SEX = 'SEX'

