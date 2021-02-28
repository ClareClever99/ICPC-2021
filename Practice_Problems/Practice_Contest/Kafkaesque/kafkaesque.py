
numSigs = int(input())
sigs = []
for i in range(numSigs):
    sigs.append(int(input()))

loops = 1
for i in range(numSigs - 1):
    if sigs[i] > sigs[i + 1]:
        loops += 1
print(loops)
