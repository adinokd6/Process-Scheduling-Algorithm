from process import Process

class Sjf_p:
    def __init__(self):
        self.process_list=[]
        self.counter=0
    def sort_list(self,list):

        n=len(list)
        list = self.sort_by_arrival_time(list)

        for i in range(n):
            for j in range(0, n - i - 1):
                if list[j].is_done() == False and list[j].return_duration()>list[j + 1].return_duration():
                    list[j], list[j + 1] = list[j + 1], list[j]


        for i in range(n):
            if list[i].return_is_running()==True:
                self.process_list.append(list[i])
            list[i].pause()

        return list

    def wait_time(self,list):
        n=len(list)
        for i in range(n):
            if  list[i].is_done() == False and list[i].return_is_running()==False:
                list[i].add_wait_time()

        return list

    def sort_by_arrival_time(self,list):
        n=len(list)
        for i in range(n):
            for j in range(0,n-i-1):
                if list[j].return_arrival_time()>list[j + 1].return_arrival_time() and list[j].is_done()==False:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list


    def make_intervals(self): #TODO indeks tablocy trzeba przypilnowac jak sie go dynamicznie zmienia
        n=len(self.process_list)
        tmp=[]
        for i in  range(n):
            print(n)
            for j in range(0,n-i-1):
                if self.process_list[j].return_id()==self.process_list[j + 1].return_id():
                    self.process_list[j].calculate_mileage()
            tmp.append(self.process_list[i])


        self.process_list=tmp




    def show(self):
        self.make_intervals()
        for i in range(len(self.process_list)):
            print("Process id: " + str(self.process_list[i].return_id()) + " Duration: " + str(self.process_list[i].return_lt()))
