from generator import Generator

class Scheduler:
    def __init__(self,state=0): #state can be read or generate (default is set to generate) e.g read=1 generate=0
        self.g=Generator(state)
        self.time = 0
        self.main_list=[]


    def check(self):
        if self.time==self.list_to_load[0].return_arrival_time():
            tmp=self.list_to_load[0]
            self.list_to_load.pop(0)
            self.main_list.append(tmp)

    def load_list(self):
        tmp_list=[]
        self.list_to_load=self.g.return_list()

    def receive_time(self,time):
        self.time=time

    def check_empty_list(self):
        if not self.main_list:
            return True
        else:
            False

    def get_process(self):












