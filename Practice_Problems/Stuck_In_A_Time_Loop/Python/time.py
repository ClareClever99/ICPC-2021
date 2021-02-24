import sys

for SystemIn in sys.stdin:
    line = SystemIn.split()
    times = int(line[0])
    for i in range(times):
        print(str(i+1) + " Abracadabra")
