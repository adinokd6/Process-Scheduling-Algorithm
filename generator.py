import numpy
import random
from process import Process


class Generator:
    def __init__(self,number_of_processes,mean_duration,standard_deviation):
        self.number_of_processes=number_of_processes
        self.mean_duration=mean_duration
        self.standard_deviation=standard_deviation
        self.random_duration()
        self.random_arrival_time()

    def read(self,file_path):
        f=open(file_path,"r")

    def write(self,file_path):
        w=open(file_path,"w")

    def new_Process(self,id,arrival_time,duration):
        tmp=Process(id,arrival_time,duration)
        return tmp

    def random_duration(self):
        arr = numpy.random.normal(loc=self.mean_duration, scale=self.standard_deviation,size=self.number_of_processes).round(0).astype(numpy.int)  # array of random duration time
        self.numbers_duration = arr.tolist()

    def random_arrival_time(self): #TODO dobrze dobrac granice losowania liczb, arrival time nie moze byc rowne sumie duration
        sum=0
        self.numbers_arrival=[]
        for i in range(len(self.numbers_duration)):
            self.numbers_arrival.append(random.randint(0, sum))
            sum = sum + self.numbers_duration[i]




    def get_duration(self):
        x=random.randint(0,len(self.numbers_duration)-1)
        tmp=self.numbers_duration[x]
        self.numbers_duration.pop(x)
        return tmp

    def get_arrival_time(self):
        x=random.randint(0,len(self.numbers_arrival)-1)
        tmp=self.numbers_arrival[x]
        self.numbers_arrival.pop(x)
        return tmp

    def generate_processes(self):
        tmp=[]
        for i in range(self.number_of_processes):
            tmp.append(self.new_Process(i,self.get_arrival_time(),self.get_duration()))

        for i in range(self.number_of_processes):
            tmp[i].print_process()
            


