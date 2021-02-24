import sys

for SystemIn in sys.stdin:
    line = SystemIn.split()
    r1 = int(line[0])
    s = int(line[1])
    print((2 * s) - r1)
