from generator import Generator
from fcfs_algorithm import Fcfs
from sjf_non_preemptive import Sjf_np
from sjf_preemtive import Sjf_p

class Scheduler:
    def __init__(self,state=0,alg=0): #state can be read or generate (default is set to generate) e.g read=1 generate=0
        self.time=0
        self.current_id=0
        self.init=True
        self.alg=alg
        self.main_list=[]
        self.algorithm()
        self.g=Generator(state)
        self.load_list()
        self.check()


    def receive_time(self,time):
        self.time=time

    def load_list(self):
        self.list_to_load=self.g.return_list()

    def get_from_list(self):
        counter = 0
        while self.list_to_load:
            if counter>(len(self.list_to_load)-1):
                break
            if self.time==self.list_to_load[counter].return_arrival_time():
                tmp = self.list_to_load[counter]
                self.list_to_load.pop(counter)
                self.main_list.append(tmp)
                self.get_from_list()
            counter = counter + 1


    def algorithm(self):
        if self.alg==0:
            self.sorting_algorithm=Fcfs()
        elif self.alg==1:
            self.sorting_algorithm=Sjf_np()
        elif self.alg==2:
            self.sorting_algorithm=Sjf_p()

    def sort(self):
        self.sorting_algorithm.sort_list(self.main_list)

    def get_process(self):
        if self.check_empty_list() == False:
            self.main_list[self.current_id].start()
            self.main_list[self.current_id].reduce_duration()

        self.main_list=self.sorting_algorithm.wait_time(self.main_list)

    def check(self):
        self.get_from_list()


        self.main_list=self.sorting_algorithm.sort_list(self.main_list)


        self.main_list[self.current_id].check_duration()

        if self.main_list[self.current_id].is_done() == True:
            if self.alg==0:
                with open("FCFS Sorted", 'a') as f:
                    f.write("Id: "+str(self.main_list[self.current_id].return_id()))
                    f.write(" Duration: "+str(self.main_list[self.current_id].return_start_duration()))
                    f.write(" Waiting time: "+str(self.main_list[self.current_id].return_waiting_time())+"\n")

            elif self.alg==1:
                with open("SJF non preemptive Sorted", 'a') as f:
                    f.write("Id: "+str(self.main_list[self.current_id].return_id()))
                    f.write(" Duration: "+str(self.main_list[self.current_id].return_start_duration()))
                    f.write(" Waiting time: "+str(self.main_list[self.current_id].return_waiting_time())+"\n")
            else:
                with open("SJF preemptive Sorted", 'a') as f:
                    f.write("Id: "+str(self.main_list[self.current_id].return_id()))
                    f.write(" Duration: "+str(self.main_list[self.current_id].return_start_duration()))
                    f.write(" Waiting time: "+str(self.main_list[self.current_id].return_waiting_time())+"\n")


            self.current_id += 1

    def check_empty_list(self):
        if self.current_id>(len(self.main_list)-1):
            return True
        else:
            return False

    def start(self):
        self.init=False

    def show(self):
        if self.alg==2:
            self.sorting_algorithm.show()
        else:
            for i in range(len(self.main_list)):
                print("Process id: "+str(self.main_list[i].return_id())+" Waiting time: " + str(self.main_list[i].return_waiting_time()))












