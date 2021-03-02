numTimes = int(input())

speedTimeList = []
speedList = []
timeList = []

totalDistance = 0

while (numTimes != -1):
    speedTimeList.clear()
    speedList.clear()
    timeList.clear()
    total = 0

    for i in range(numTimes):
        speedTimeList.append(input())
    for item in speedTimeList:
        speedList.append(int(item.split(" ")[0]))
        timeList.append(int(item.split(" ")[1]))
    total += speedList[0] * timeList[0]
    for i in range(numTimes-1):
        total += ((timeList[i+1]) - timeList[i]) * speedList[i+1]
    print(total, "miles")
    numTimes = int(input())
    
