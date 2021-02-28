numSigs = int(input())
sigs = []
for i in range(numSigs):
    sigs.append(int(input()))

completedSigs = 0
currPos = 0
loopCount = 1

while(completedSigs < numSigs):
    currPos += 1
    if currPos == 100:
        currPos = 1
        loopCount += 1

    if currPos == sigs[completedSigs]:
        completedSigs += 1

print(loopCount)
