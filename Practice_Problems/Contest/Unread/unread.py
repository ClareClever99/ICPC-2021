line1 = input().split(" ")
n = int(line1[0])
m = int(line1[1])
lastIndex = [0] * n
unread = 0
for i in range(m):
    num = int(input())
    unread += (n - 1) - (i - lastIndex[num - 1])
    lastIndex[num - 1] = i + 1
    print(str(unread))
