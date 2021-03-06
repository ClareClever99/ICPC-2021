inputCount = int(input())
playerSkills = []
playerLimits = []

for i in range(inputCount):
	line = input()
	lineList = line.split(" ")
	playerSkills.append(int(lineList[0])) 
	playerLimits.append(int(lineList[1]))
	
maxExcitement = 0
minExcitement = 10000
	
while len(playerSkills) >= 2:
	maxXor = 0
	minXor = 10000
	
	i2 = 0
	i3 = 0
	
	j2 = 0
	j3 = 0
	
	for i in range(len(playerSkills)): 
		for j in range(i + 1, len(playerSkills)): 
			currXor = playerSkills[i] ^ playerSkills[j]
			if currXor > maxXor:
				maxXor = currXor
				i2 = i
				j2 = j
			elif currXor < minXor:
				minXor = currXor
				i3 = i
				j3 = j
				
	playerLimits[i2] -= 1
	if playerLimits[i2] == 0:
		playerLimits.pop(i2)
		playerSkills.pop(i2)
		if i2 < j2:
			j2 -= 1
		if i2 < i3:
			i3 -= 1
		if i2 < j3:
			j3 -= 1
		
	playerLimits[j2] -= 1
	if playerLimits[j2] == 0:
		playerLimits.pop(j2)
		playerSkills.pop(j2)
		if j2 < i2:
			i2 -= 1
		if j2 < i3:
			i3 -= 1
		if j2 < j3:
			j3 -= 1
		
	playerLimits[i3] -= 1
	if playerLimits[i3] == 0:
		playerLimits.pop(i3)
		playerSkills.pop(i3)
		if i3 < j2:
			j2 -= 1
		if i3 < i2:
			i2 -= 1
		if i3 < j3:
			j3 -= 1
		
	playerLimits[j3] -= 1
	if playerLimits[j3] == 0:
		playerLimits.pop(j3)
		playerSkills.pop(j3)
		if j3 < j2:
			j2 -= 1
		if j3 < i3:
			i3 -= 1
		if j3 < i2:
			i2 -= 1
		
	maxExcitement += maxXor
	minExcitement += minXor
	
print(minExcitement, maxExcitement)
	

	
	
	
	
				
	
