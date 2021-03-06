inputCount = int(input())
lengths = []

for i in range(inputCount):
    lengths.append(int(input()))

validCount = 0

for i in range(inputCount-2):
    for j in range(i+1, inputCount-1, 1):
        for k in range(j+1, inputCount, 1):
            if lengths[i] + lengths[j] > lengths[k] and lengths[i] + lengths[k] > lengths[j] and lengths[j] + lengths[k] > lengths[i]:
                validCount += 1

print(validCount)
