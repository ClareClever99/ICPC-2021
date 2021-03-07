line1 = input().split(" ")
n = int(line1[0])
m = int(line1[1])
lastIndex = {}
unread = 0
for i in range(m):
	num = int(input())
	if (num - 1) in lastIndex:
		unread += (n - 1) - (i - lastIndex[(num - 1)])
	else:
		unread += (n - 1) - i
	lastIndex[(num - 1)] = i + 1
	print(str(unread))
