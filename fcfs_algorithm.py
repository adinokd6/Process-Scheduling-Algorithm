
class Fcfs:
    def __init__(self):
        self.list_to_sort=[]

    def add_to_list(self,process):
        self.list_to_sort.append(process)

    def return_list(self):
        return self.list_to_sort


