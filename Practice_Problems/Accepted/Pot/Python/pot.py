numNumbers = int(input())

listOfNumbers = []

total = 0

for i in range(numNumbers):
    listOfNumbers.append(input())

for num in listOfNumbers:
    number = num[0:len(num)-1]
    power = num[-1]
    total += int(number)**int(power)

print(total)
