n = int(input())
heights = [0] * n
pairs = 0
for i in range(n):
    heights[i] = int(input())

for i in range(n - 1):
    height1 = heights[i]
    maxHeight = heights[i + 1]
    for j in range(i + 1, n):
        height2 = heights[j]
        if height2 > height1:
            if height1 > maxHeight:
                pairs += 1
            break
        else:
            if height2 > maxHeight:
                pairs += 1
                maxHeight = height2
    
pairs += n - 1
print(pairs)