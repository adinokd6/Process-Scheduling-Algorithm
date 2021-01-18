

class Process:
    def __init__(self,id,arrival_time,duration):
        self.id=id
        self.last_time=0
        self.duration=duration
        self.start_duration=duration
        self.arrival_time=arrival_time
        self.waiting_time=0
        self.end_time=0
        self.processing_time=0
        self.is_running=False
        self.ended=False

    def start(self):
        self.is_running=True

    def pause(self):
        self.is_running=False

    def calculate_mileage(self):
        self.last_time = self.last_time +1

    def return_lt(self):
        return self.last_time

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
            self.is_running=False

    def return_arrival_time(self):
        return self.arrival_time

    def return_duration(self):
        return self.duration

    def return_start_duration(self):
        return self.start_duration

    def return_waiting_time(self):
        return self.waiting_time

    def return_id(self):
        return self.id

    def return_is_running(self):
        return self.is_running

    def write_end_time(self,time):
        self.end_time=time

    def calculate_processing_time(self):
        self.processing_time=self.end_time-self.arrival_time

    def return_processing_time(self):
        return self.processing_time

    def return_end_time(self):
        return self.end_time

    def print_p(self):
        print("Id: "+str(self.id)+" Is done: "+str(self.is_done()))

    def print_pr(self):
        print("Id: " + str(self.id) + " Duration: " + str(self.return_duration()))
