string = input()
chars = []
out = 1
for i in range(len(string)):
    if string[i] not in chars:
        chars.append(string[i])
    else:
        out = 0
        break
print(str(out))
