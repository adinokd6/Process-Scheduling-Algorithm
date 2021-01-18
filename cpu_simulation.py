from scheduler import Scheduler

generate=0
read=1
sjf=1
sjf_p=2
fcfs=0

class CPU:
    def __init__(self,trybe,algorithm):
        self.cycle=0
        self.s=Scheduler(trybe,algorithm)
        self.s.start()

    def do_cycle(self):
        if self.s.check_empty_list()==False:
            self.s.check()
            self.s.get_process()
            self.cycle += 1
            self.s.receive_time(self.cycle)
            return True
        else:
            self.s.calculate()
            return False




    def run(self):
        while True:
            if self.do_cycle()==False:
                break

        self.s.show()


