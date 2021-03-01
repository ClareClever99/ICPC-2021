numNumbers = int(input())

numbers = []

for i in range(numNumbers):
    numbers.append(input())

index = len(numbers) - 1

for number in numbers:
    print(numbers[index])
    index -= 1
