from scheduler import Scheduler

class CPU:
    def __init__(self):
        self.cycle=0
        self.s=Scheduler()

    def do_cycle(self):
        self.s.get_process()
        self.cycle=self.cycle+1
        if self.s.check_empty_list()==False:
            return True

    def run(self):
        while True:
            self.do_cycle()


