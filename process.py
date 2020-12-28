

class Process:
    def __init__(self,id,arrival_time,duration):
        self.id=id
        self.duration=duration
        self.arrival_time=arrival_time
        self.waiting_time=0
        self.is_done=False

    def write_wait_time(self,wait_time):
        self.waiting_time=wait_time

    def remaining_duration(self,duration):
        self.duration-=duration

    def is_done(self,state):
        return self.is_done

    def check_duration(self):
        if self.duration==0:
            self.is_done=True

    def return_arrival_time(self):
        return self.arrival_time

    def return_duration(self):
        return self.duration

    def return_waiting_time(self):
        return self.waiting_time
