import attributes
from human import human
import values

if __name__ == '__main__':
    
    PAUL_BODY = attributes.BodyState(
        GENDER=values.GENDER.MALE,
        WEIGHT=80,
        HEIGHT=180,
        AGE=34,
        NAME=values.NAME.ALEX
        )
    
    PAUL_JOB = attributes.JobState(
        OCCUPATION=values.OCCUPATION.DOCTOR,
        SALARY=60_000,
        WORK_H_PER_WEEK=36
        )
    
    PAUL_MISC = attributes.MiscState(
        DRIVERS_LICENSE=True,
        SEXUALLY_ACTIVE=False,
        SCREENTIME_PER_DAY=2.21,
        GOAL=values.GOAL.BECOME_RICH
        )
    
    PAUL_ACTIVITY = attributes.ActivityState(
        CURRENT_ACTIVITY=values.ACTIVITY.SLEEP
        )
    
    Paul = human(body=PAUL_BODY, job=PAUL_JOB, activity=PAUL_ACTIVITY, misc=PAUL_MISC)
    
    
    
    print(Paul.job.OCCUPATION)
    