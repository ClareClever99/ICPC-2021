inp = str(input())

inp = inp.split(" ")
n = int(inp[0])
h = int(inp[1])
v = int(inp[2])
if (h > n/2):
    if (v > n/2):
        print(str(h * v * 4))
    else:
        print(str(h * (n - v) * 4))
else:
    if (v > n/2):
        print(str((n - h) * v * 4))
    else:
        print(str((n - h) * (n - v) * 4))
