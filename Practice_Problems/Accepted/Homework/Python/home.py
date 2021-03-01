valueIn = input()

splitInput = valueIn.split(";")

totalProblems = 0

for problemSet in splitInput:
    if "-" in problemSet:
        numbersInRange = problemSet.split("-")
        totalProblems += (int(numbersInRange[1]) - int(numbersInRange[0])) + 1
    else:
        totalProblems += 1

print(totalProblems)
