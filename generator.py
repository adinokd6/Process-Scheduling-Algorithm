import numpy
import random
from process import Process


class Generator:
    def __init__(self,state=0): #state can be read or generate (default is set to generate) e.g read=1 generate=0
        if state==0:
            self.set_conditions()
        else:
            f=input("File path: ")
            self.file_path=f
            self.read()


    def set_conditions(self):
        number_of_processes=int(input("Liczba procesow: "))
        mean_duration=int(input("Srednia wartosc: "))
        standard_deviation=int(input("Odchylenie standardowe: "))
        self.number_of_processes=number_of_processes
        self.mean_duration=mean_duration
        self.standard_deviation=standard_deviation
        self.numbers_duration=[]
        self.random_duration()
        self.random_arrival_time()
        self.generate_processes()

    def read(self):
        f=open(self.file_path,'r').read()
        lines=f.split('\n')    #
        lines.pop(len(lines)-1)

        tmp_processes=[]

        for line in lines:
            tmp=line.split(" ")
            tmp_id=int(tmp[0])
            tmp_arrival_time=int(tmp[1])
            tmp_duration=int(tmp[2])
            tmp_processes.append(self.new_Process(tmp_id,tmp_arrival_time,tmp_duration))

        self.list_of_processes=tmp_processes

    def return_list(self):
        return self.list_of_processes

    def is_empty(self):
        if not self.list_of_processes:
            return True
        else:
            return False

    def remove_process(self,number):
        self.list_of_processes.pop(number)

    def write(self,file_path):
        w=open(file_path,"w")

    def new_Process(self,id,arrival_time,duration):
        tmp=Process(id,arrival_time,duration)
        return tmp

    def random_duration(self): #TODO generator losuje liczby i duration niekiedy wynosi 0. Trzeba to jakos naprawic
        arr = numpy.random.normal(loc=self.mean_duration, scale=self.standard_deviation,size=(self.number_of_processes+100)).round(0).astype(numpy.int)  # array of random duration time
        tmp_arr=arr.tolist()
        var=0
        for i in range(self.number_of_processes):
            while var <= 0:
                var = random.choice(tmp_arr)
            self.numbers_duration.append(var)
            var=0

    def random_arrival_time(self):
        sum=0
        self.numbers_arrival=[]
        set_of_arrivals=set()

        for i in range(len(self.numbers_duration)):
            tmp=random.randint(0,sum) #
            while tmp in set_of_arrivals:
                tmp=random.randint(0,sum)

            set_of_arrivals.add(tmp)

            self.numbers_arrival.append(tmp)
            sum = sum + self.numbers_duration[i]

        arr=numpy.array(self.numbers_arrival)
        tmp=numpy.sort(arr)
        self.numbers_arrival=tmp.tolist()


    def get_duration(self):
        x=random.randint(0,len(self.numbers_duration)-1)
        tmp=self.numbers_duration[x]
        self.numbers_duration.pop(x)
        return tmp

    def get_arrival_time(self):
        tmp=self.numbers_arrival[0]
        self.numbers_arrival.pop(0)
        return tmp

    def generate_processes(self):
        tmp=[]
        for i in range(self.number_of_processes):
            tmp_id=i+1
            tmp.append(self.new_Process(tmp_id,self.get_arrival_time(),self.get_duration()))

        self.list_of_processes=tmp
            


