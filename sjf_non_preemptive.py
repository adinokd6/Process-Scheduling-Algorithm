from process import Process
from random import randint

class Sjf_np:
    def sort_list(self,list):
        n=len(list)
        list=self.sort_by_arrival_time(list)
        #5/CyLQNAve0YQhMuexWN5EarH6XWI/aFwJ7MPX17tz0='

        list=sorted(list,key=lambda p: (p.done_sjf(),p.run_sjf(),p.return_duration()))

        return list

    def wait_time(self,list):
        n=len(list)
        for i in range(n):
            if list[i].return_is_running() == False and list[i].is_done() == False:
                list[i].add_wait_time()

        return list

    def sort_by_arrival_time(self,list):

        sorted(list,key=(lambda p: p.return_arrival_time() and p.return_is_running()==False and p.is_done()==False))

        return list

