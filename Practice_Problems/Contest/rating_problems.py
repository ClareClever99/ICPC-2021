initialinput = input().split(" ")
totalJudges = int(initialinput[0])
currentJudges = int(initialinput[1])

rating = 0

for i in range(currentJudges):
    rating += int(input())

minRating = (rating + (-3 * (totalJudges - currentJudges))) / totalJudges
maxRating = (rating + (3 * (totalJudges - currentJudges))) / totalJudges

print(str(minRating) + " " + str(maxRating))
