import sys

for SystemIn in sys.stdin:
    line = SystemIn.split()
    stones = int(line[0])
    if (stones % 2):
        print("Alice")
    else:
        print("Bob")
