contestantOne = input()
contestantTwo = input()
contestantThree = input()
contestantFour = input()
contestantFive = input()

contestantOne = contestantOne.split(" ")
contestantTwo = contestantTwo.split(" ")
contestantThree = contestantThree.split(" ")
contestantFour = contestantFour.split(" ")
contestantFive = contestantFive.split(" ")

contestantOneScore = 0
contestantTwoScore = 0
contestantThreeScore = 0
contestantFourScore = 0
contestantFiveScore = 0

for item in contestantOne:
    contestantOneScore += int(item)
for item in contestantTwo:
    contestantTwoScore += int(item)
for item in contestantThree:
    contestantThreeScore += int(item)
for item in contestantFour:
    contestantFourScore += int(item)
for item in contestantFive:
    contestantFiveScore += int(item)

my_dict = {
    "1": contestantOneScore,
    "2": contestantTwoScore,
    "3": contestantThreeScore,
    "4": contestantFourScore,
    "5": contestantFiveScore,
}

# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())

maxValue = max(val_list)

position = val_list.index(maxValue)

print(key_list[position], maxValue)
