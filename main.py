from cpu_simulation import CPU


generate=0
read=1
sjf=1
sjf_p=2
fcfs=0



tmp=1
while tmp!=0:
    algorithm = int(input("Jaki algorytm? 0-FCFS 1-SJF 2-SJF_P: "))
    trybe=int(input("Jaki tryb? Generator-0 Odczyt z pliku-1: "))
    c = CPU(trybe,algorithm)
    c.run()
    tmp=int(input("Dalej? 1-Tak 0-Nie: "))
    continue
