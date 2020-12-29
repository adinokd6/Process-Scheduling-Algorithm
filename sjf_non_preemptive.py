from process import Process

class Sjf_np:
    def __init__(self):
        self.list= []

    def return_list(self):
        return self.list

    def add_to_list(self,Process): #return_duration
        self.list.append(Process)
        self.sort_list()

    def delete_process(self,id):
        print("Dlugosc tablicy: "+str(len(self.list)))
        for i in range(len(self.list)):
            print("Eureka")
            print("Zwrocona wart: "+str(self.list[len(self.list)].return_id()))
            if self.list[i].return_id()==id:
                self.list.pop(i)
        self.sort_list()

    def sort_list(self):
        n=len(self.list)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.list[j].return_duration() > self.list[j + 1].return_duration() and self.list[j].return_arrival_time():
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]