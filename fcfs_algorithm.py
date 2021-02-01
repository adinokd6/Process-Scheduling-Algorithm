
class Fcfs:

    def sort_list(self,list):

        sorted(list,key=(lambda p:p.return_arrival_time() and p.return_is_running()==False and p.is_done()==False))

        return list

    def wait_time(self,list):
        n=len(list)
        for i in range(n):
            if list[i].return_is_running() == False and list[i].is_done() == False:
                list[i].add_wait_time()

        return list



