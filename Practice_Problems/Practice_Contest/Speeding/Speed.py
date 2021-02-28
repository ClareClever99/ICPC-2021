
photoCount = int(input())
photos = []

for i in range(photoCount):
    photos.append(input())

prevPhoto = 0
currPhoto = 1
highestSpeed = 0

while(currPhoto < photoCount):
    time = int((photos[currPhoto].split(" "))[0])
    distance = int((photos[currPhoto].split(" "))[1])

    prevTime = int((photos[prevPhoto].split(" "))[0])
    prevDistance = int((photos[prevPhoto].split(" "))[1])

    currSpeed = ((distance - prevDistance) / (time - prevTime))

    if(currSpeed > highestSpeed):
        highestSpeed = currSpeed

    currPhoto += 1
    prevPhoto += 1

print(int(highestSpeed))
