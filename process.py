

class Process:
    def __init__(self,id,arrival_time,duration):
        self.id=id
        self.duration=duration
        self.starting_duration=duration
        self.arrival_time=arrival_time
        self.waiting_time=0
        self.ended=False

    def write_wait_time(self,waiting_time):
        self.waiting_time=waiting_time

    def add_wait_time(self):
        self.waiting_time+=1

    def reduce_duration(self):
        self.duration-=1

    def is_done(self):
        return self.ended

    def check_duration(self):
        if self.duration==0:
            self.ended=True

    def return_arrival_time(self):
        return self.arrival_time

    def return_duration(self):
        return self.duration

    def return_waiting_time(self):
        return self.waiting_time

    def return_id(self):
        return self.id

    def return_starting_duration(self):
        return self.starting_duration

    def print_p(self):
        print(str(self.id)+" Arrival time: "+str(self.arrival_time)+" Duration: "+str(self.duration))
