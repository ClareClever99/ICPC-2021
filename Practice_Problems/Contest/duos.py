n = int(input())
heights = []
pairs = 0
for i in range(n):
    heights.append(int(input()))

for i in range(n):
    for j in range(i + 1, n):
        lastK = i + 1
        for k in range(i + 1, j):
            lastK = k
            if heights[i] > heights[j]:
                if heights[j] < heights[k]:
                    break

            else:
                if heights[i] < heights[k]:
                    break
        else:
            pairs += 1
        if heights[i] < heights[lastK]:
            break

print(pairs)
