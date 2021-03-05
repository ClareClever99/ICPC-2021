message = input()

total = 0
whitespace = 0
lowercase = 0
uppercase = 0
symbol = 0

for char in message:
    total += 1
    if ord(char) == 95:
        whitespace += 1
    elif ord(char) >= 97 and ord(char) <= 122:
        lowercase += 1
    elif ord(char) >= 65 and ord(char) <= 90:
        uppercase += 1
    else:
        symbol += 1

print(str(whitespace/total) + "\n" + str(lowercase/total) + "\n" +
      str(uppercase/total) + "\n" + str(symbol/total))
