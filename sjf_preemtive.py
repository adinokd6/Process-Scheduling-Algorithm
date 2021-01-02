
class Sjf_p:
    def return_list(self):
        return self.list_to_sort

    def sort_by_arrival_time(self,list):
        n=len(self.list)
        for i in range(n):
            for j in range(0,n-i-1):
                if self.list[j].return_arrival_time()>self.list[j + 1].return_arrival_time():
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
