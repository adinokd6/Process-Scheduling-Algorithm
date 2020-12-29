from scheduler import Scheduler

generate=0
read=1
sjf=1
sjf_p=2
fcfs=0

class CPU:
    def __init__(self):
        self.cycle=0
        self.s=Scheduler(generate,sjf)

    def do_cycle(self):
        if self.s.check_empty_list()==False:
            self.s.check()
            self.cycle+=1
            self.s.receive_time(self.cycle)
            self.s.get_process()
            return True
        else:
            return False




    def run(self):
        while True:
            if self.do_cycle()==False:
                break

        self.s.my()


