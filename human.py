import abc
import attributes as A

class human(abc.ABC):
    
    def __init__(self, body: A.BodyState, job: A.JobState, activity: A.ActivityState, misc: A.MiscState):
        self.body = body
        self.job = job
        self.activity = activity
        self.misc = misc
    
    def do(self):
        pass
    
    def receive(self):
        pass
        


class human(human):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    
