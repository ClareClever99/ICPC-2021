numLines = int(input())

inputNumbers = []

total = 0

for i in range(numLines):
    inputNumbers.append(input())

for number in inputNumbers:
    print(type(number))

print(inputNumbers)
