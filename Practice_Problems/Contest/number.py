def lessTen(string):
    for i in range(length):
        if i < (length - 1):
            if (i + 1) != int(string[i]):
                print(i + 1)
                break
        else:
            print(length)
            break


length = int(input())
string = input()
s = len(string)

if length < 10:
    lessTen(string)
else:
    if int(string[8]) != 9:
        lessTen(string)
    else:
        init = 9
        run = False
        for i in range(9, s, 2):
            if (init + 1) != int(string[i:i + 2]):
                run = True
                print(init + 1)
                break
            init += 1
        if not(run):
            print(length)
