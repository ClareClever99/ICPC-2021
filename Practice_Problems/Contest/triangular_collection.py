inputCount = int(input())
lengths = []

for i in range(inputCount):
    lengths.append(int(input()))

validCount = 0

for i in range(inputCount):
    for j in range(inputCount):
        for k in range(inputCount):
            if i != j and j != k and i != k:
                if lengths[i] + lengths[j] > lengths[k] and lengths[i] + lengths[k] > lengths[j] and lengths[j] + lengths[k] > lengths[i]:
                    validCount += 1

print(validCount)
