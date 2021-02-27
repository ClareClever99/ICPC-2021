textIn = input()

numberOfE = textIn.count("e")

newString = "h"

for i in range(0, numberOfE * 2):
    newString += "e"

newString += "y"

print(newString)
