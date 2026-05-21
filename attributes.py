from dataclasses import dataclass
import values

@dataclass
class BodyState:
    NAME: values.NAME
    GENDER: values.GENDER
    WEIGHT: float
    HEIGHT: float
    AGE: int
    
    def __post_init__(self):
        if not (10 <= self.WEIGHT <= 175):
            raise ValueError('[WARNING] WEIGHT MUST BE IN APPROPIATE RANGE!')
        if not (50 <= self.HEIGHT <= 225):
            raise ValueError('[WARNING] HEIGHT MUST BE IN APPROPIATE RANGE!')
        if not (1 <= self.AGE <= 100):
            raise ValueError('[WARNING] AGE MUST BE IN APPROPIATE RANGE!')
        

@dataclass
class JobState:
    OCCUPATION: values.OCCUPATION
    SALARY: int
    WORK_H_PER_WEEK: int
    
    def __post_init__(self):
        if not (0 <= self.SALARY <= 1_000_000):
            raise ValueError('[WARNING] SALARY MUST BE IN APPROPIATE RANGE!')
        if not (0 <= self.WORK_H_PER_WEEK <= 85):
            raise ValueError('[WARNING] WORK_H_PER_WEEK MUST BE IN APPROPIATE RANGE!')
@dataclass
class MiscState:
    DRIVERS_LICENSE: bool
    SEXUALLY_ACTIVE: bool
    SCREENTIME_PER_DAY: float
    GOAL: values.GOAL
    
    def __post_init__(self):
        if not (0 <= self.SCREENTIME_PER_DAY <= 10):
            raise ValueError('[WARNING] SCREENTIME_PER_DAY MUST BE IN APPROPIATE RANGE!')
    
@dataclass
class ActivityState:
    CURRENT_ACTIVITY: values.ACTIVITY
    