roll = input()
dice = roll.split(" ")
dice[0] = int(dice[0])
dice[1] = int(dice[1])
dice.sort()

for i in range(int(dice[0])+1, int(dice[1])+2, 1):
    print(i)
