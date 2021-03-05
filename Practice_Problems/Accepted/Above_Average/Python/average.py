inputcount = int(input())
lines = []

for i in range(inputcount):
    lines.append(input())

for line in lines:
    linelist = line.split(" ")
    count = int(linelist[0])
    linelist = linelist[1:]
    total = 0
    avgcount = 0
    for num in linelist:
        total += int(num)
    avg = total/count
    for num in linelist:
        if int(num) > avg:
            avgcount += 1
    number = (avgcount/count)*100
    print(format(number, ".3f")+"%")
