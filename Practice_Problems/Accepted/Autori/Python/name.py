name = input()

nameSplit = name.split("-")

newString = ""

for name in nameSplit:
    newString += name[0]

print(newString)
