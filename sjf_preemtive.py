from process import Process
import copy

class Sjf_p:
    def __init__(self):
        self.process_list=[]
        self.counter=0

    def sort_list(self,list):

        n=len(list)
        list = self.sort_by_arrival_time(list)

        list.sort(key=(lambda p: p.is_done()==False and p.return_duration()))


        for i in range(n):
            if list[i].return_is_running()==True:
                self.process_list.append(copy.copy(list[i]))
            list[i].pause()

        return list

    def wait_time(self,list):
        n=len(list)
        for i in range(n):
            if  list[i].is_done() == False and list[i].return_is_running()==False:
                list[i].add_wait_time()

        return list

    def sort_by_arrival_time(self,list):
        sorted(list,key=(lambda p: p.return_arrival_time() and p.return_is_running() == False and p.is_done() == False))
        return list


    def show(self):
        for i in range(len(self.process_list)):
            print("Process id: " + str(self.process_list[i].return_id()) + " Duration: " + str(self.process_list[i].return_duration()))
