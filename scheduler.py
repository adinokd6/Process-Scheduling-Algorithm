from generator import Generator
from fcfs_algorithm import Fcfs

class Scheduler:
    def __init__(self,state=0,alg=0): #state can be read or generate (default is set to generate) e.g read=1 generate=0
        self.g=Generator(state)
        self.load_list()
        self.time=0
        self.alg=alg
        self.algorithm()
        self.check()



    def check(self):

        if not self.list_to_load:
            pass
        else:
            if self.time==self.list_to_load[0].return_arrival_time():
                tmp=self.list_to_load[0]
                self.list_to_load.pop(0)
                self.sorting_algorithm.add_to_list(tmp)
                self.main_list=self.sorting_algorithm.return_list()



    def load_list(self):
        tmp_list=[]
        self.list_to_load=self.g.return_list()
        for i in range(len(self.list_to_load)):
            self.list_to_load[i].print_p()

    def return_list(self):
        return self.main_list

    def update_list(self,new_list):
        self.main_list=new_list

    def receive_time(self,time):
        self.time=time

    def check_empty_list(self):
        if not self.main_list:
            return True
        else:
            return False

    def get_process(self):
        self.main_list[0].reduce_duration()
        if self.main_list[0].return_duration()==0:
            self.main_list.pop(0)

    def algorithm(self):
        if self.alg==0:
            self.sorting_algorithm=Fcfs()
        else:
            i=0












