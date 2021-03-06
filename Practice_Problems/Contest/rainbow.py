def isRainbow(string):
    n = len(string)
    if n == 1:
        return True
    elif n == 2 and int(string) % 11 == 0:
        return False
    else:
        return string[n//2] != string[n//2 - 1] and isRainbow(string[0:n//2]) and isRainbow(string[n//2:n])


L = int(input())
U = int(input())
num = 0
for i in range(L, U + 1):
    if isRainbow(str(i)):
        num += 1
print(num % 998244353)
