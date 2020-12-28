from generator import Generator


k=Generator(0)

tmp=k.list_of_processes

for i in range(len(tmp)):
    tmp[i].print_p()
