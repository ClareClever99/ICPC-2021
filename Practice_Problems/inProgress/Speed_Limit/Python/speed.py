numTimes = int(input())

speedTimeList = []
speedList = []
timeList = []

temp = ""

totalDistance = 0

while (numTimes != -1):
    for i in range(numTimes):
        speedTimeList.append(input())
    for item in speedTimeList:
        split = item.split()
        speedList.append(split[0])
        timeList.append(split[1])
    print(speedList, timeList)
    numTimes = int(input())
