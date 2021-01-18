from generator import Generator
import numpy
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
                #5/CyLQNAve0YQhMuexWN5EarH6XWI/aFwJ7MPX17tz0=
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
            self.write_to_file()


            self.current_id += 1

    def check_empty_list(self):
        if self.current_id>(len(self.main_list)-1):
            return True
        else:
            return False

    def start(self):
        self.init=False


    def write_to_file(self):
        self.main_list[self.current_id].write_end_time(self.time)
        self.main_list[self.current_id].calculate_processing_time()
        if self.alg == 0:
            with open("FCFS Sorted", 'a') as f:
                f.write("Id: " + str(self.main_list[self.current_id].return_id()))
                f.write(" Duration: " + str(self.main_list[self.current_id].return_start_duration()))
                f.write(" Waiting time: " + str(self.main_list[self.current_id].return_waiting_time()))
                f.write(" End time: " + str(self.main_list[self.current_id].return_end_time()))
                f.write(" Processing time: " + str(self.main_list[self.current_id].return_processing_time()) + "\n")

        elif self.alg == 1:
            with open("SJF non preemptive Sorted", 'a') as f:
                f.write("Id: " + str(self.main_list[self.current_id].return_id()))
                f.write(" Duration: " + str(self.main_list[self.current_id].return_start_duration()))
                f.write(" Waiting time: " + str(self.main_list[self.current_id].return_waiting_time()))
                f.write(" End time: " + str(self.main_list[self.current_id].return_end_time()))
                f.write(" Processing time: " + str(self.main_list[self.current_id].return_processing_time()) + "\n")
        else:
            with open("SJF preemptive Sorted", 'a') as f:
                f.write("Id: " + str(self.main_list[self.current_id].return_id()))
                f.write(" Duration: " + str(self.main_list[self.current_id].return_start_duration()))
                f.write(" Waiting time: " + str(self.main_list[self.current_id].return_waiting_time()))
                f.write(" End time: " + str(self.main_list[self.current_id].return_end_time()))
                f.write(" Processing time: " + str(self.main_list[self.current_id].return_processing_time()) + "\n")


    def calculate(self):
        tmp_duration=[]
        tmp_processing_time=[]
        tmp_waiting_time=[]
        for i in range(len(self.main_list)):
            tmp_duration.append(self.main_list[i].return_start_duration())
            tmp_processing_time.append(self.main_list[i].return_processing_time())
            tmp_waiting_time.append(self.main_list[i].return_waiting_time())
        # numpy_duration=numpy.array(tmp_duration)
        # numpy_processing_time=numpy.array(tmp_processing_time)
        # numpy_waiting_time=numpy.array(tmp_waiting_time)
        if self.alg == 0:
            with open("FCFS Sorted", 'a') as f:
                f.write("Sum of duration: "+str(numpy.sum(tmp_duration))+" Average duration: "+str(numpy.mean(tmp_duration).round(2))+" Standard deviation: +/- "+str(numpy.std(tmp_duration).round(2)))
                f.write("Sum of waiting time: " +str(numpy.sum(tmp_waiting_time))+" Average waiting time: " +str(numpy.mean(tmp_waiting_time).round(2))+" Standard deviation: +/- " +str(numpy.std(tmp_waiting_time).round(2)))
                f.write("Sum of processing time: " +str(numpy.sum(tmp_processing_time))+" Average processing time: " +str(numpy.mean(tmp_processing_time).round(2))+" Standard deviation: +/- " +str(numpy.std(tmp_processing_time).round(2)))
        elif self.alg == 1:
            with open("SJF non preemptive Sorted", 'a') as f:
                f.write("Sum of duration: "+str(numpy.sum(tmp_duration))+" Average duration: "+str(numpy.mean(tmp_duration).round(2))+" Standard deviation: +/- "+str(numpy.std(tmp_duration).round(2)))
                f.write("Sum of waiting time: " +str(numpy.sum(tmp_waiting_time))+" Average waiting time: " +str(numpy.mean(tmp_waiting_time).round(2))+" Standard deviation: +/- " +str(numpy.std(tmp_waiting_time).round(2)))
                f.write("Sum of processing time: " +str(numpy.sum(tmp_processing_time))+" Average processing time: " +str(numpy.mean(tmp_processing_time).round(2))+" Standard deviation: +/- " +str(numpy.std(tmp_processing_time).round(2)))
        else:
            with open("SJF preemptive Sorted", 'a') as f:
                f.write("Sum of duration: "+str(numpy.sum(tmp_duration))+" Average duration: "+str(numpy.mean(tmp_duration).round(2))+" Standard deviation: +/- "+str(numpy.std(tmp_duration).round(2)))
                f.write("Sum of waiting time: " +str(numpy.sum(tmp_waiting_time))+" Average waiting time: " +str(numpy.mean(tmp_waiting_time).round(2))+" Standard deviation: +/- " +str(numpy.std(tmp_waiting_time).round(2)))
                f.write("Sum of processing time: " +str(numpy.sum(tmp_processing_time))+" Average processing time: " +str(numpy.mean(tmp_processing_time).round(2))+" Standard deviation: +/- " +str(numpy.std(tmp_processing_time).round(2)))


    def show(self):
        if self.alg==2:
            self.sorting_algorithm.show()
        else:
            for i in range(len(self.main_list)):
                print("Process id: "+str(self.main_list[i].return_id())+" Waiting time: " + str(self.main_list[i].return_waiting_time()))












