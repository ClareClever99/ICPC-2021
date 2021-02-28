
photoCount = int(input())
photos = []
currenSpeed = []

for i in range(photoCount):
    photos.append(input())

currPhoto = 0
highestSpeed = 0

while(currPhoto < photoCount):
    time = int((photos[currPhoto].split(" "))[0])
    distance = int((photos[currPhoto].split(" "))[1])
    if (time != 0 and distance != 0):
        currenSpeed.append(distance/time)
        if(currSpeed > highestSpeed):
            highestSpeed = currSpeed
    currPhoto += 1

print(int(highestSpeed))
