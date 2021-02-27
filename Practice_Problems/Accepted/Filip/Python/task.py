inputString = input()
values = inputString.split()


def swapFL(num):
    newnum = ""
    newnum += num[2]
    newnum += num[1]
    newnum += num[0]
    return newnum


first = int(swapFL(values[0]))
last = int(swapFL(values[1]))

print(max(first, last))
