from generator import Generator
from fcfs_algorithm import Fcfs
from sjf_non_preemptive import Sjf_np

class Scheduler:
    def __init__(self,state=0,alg=0): #state can be read or generate (default is set to generate) e.g read=1 generate=0
        self.id=0
        self.time=0
        self.g=Generator(state)
        self.load_list()
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

        if self.alg==1 and self.main_list[self.id].is_done()==True:
            tmp = self.main_list[self.id].return_id()
            self.sorting_algorithm.delete_process(tmp)



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
        if self.id>(len(self.main_list)-1):
            return True

        else:
            return False

    def next_process(self):
        self.id+=1


    def get_process(self):
        self.main_list[self.id].reduce_duration()
        if self.main_list[self.id].return_duration()==0:
            self.main_list[self.id].check_duration()
            self.next_process()
            if self.check_empty_list()==False:
                self.calculate_waiting_time()

    def calculate_waiting_time(self):
        if self.alg==0:
            tmp=0
            for i in range(len(self.main_list)):
                self.main_list[i].write_wait_time(tmp)
                tmp+=self.main_list[i].return_starting_duration()
        elif self.alg==1:
            tmp_time_line=0
            for i in range(len(self.main_list)):
                tmp_wait_time=tmp_time_line-self.main_list[i].return_arrival_time()
                self.main_list[i].write_wait_time(tmp_wait_time)
                tmp_time_line+=self.main_list[i].return_starting_duration()
        else:
            print("Dupa")


    def algorithm(self):
        if self.alg==0:
            self.sorting_algorithm=Fcfs()
        elif self.alg==1:
            self.sorting_algorithm=Sjf_np()

    def my(self):
        for i in range(len(self.main_list)):
            print("Process id: "+str(self.main_list[i].return_id())+" Waiting time: " + str(self.main_list[i].return_waiting_time())+" Duration: "+str(self.main_list[i].return_starting_duration())+" Arrival time: "+str(self.main_list[i].return_arrival_time()))












