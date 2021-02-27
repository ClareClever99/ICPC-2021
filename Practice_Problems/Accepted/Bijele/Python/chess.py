pieces = input()

piecesSplit = pieces.split(" ")

king, queen, rooks, bishops, knights, pawns = 0, 0, 0, 0, 0, 0

if (int(piecesSplit[0]) < 1):
    king = abs(int(piecesSplit[0]) - 1)
elif (int(piecesSplit[0]) > 1):
    king = -(int(piecesSplit[0]) - 1)

if (int(piecesSplit[1]) < 1):
    queen = abs(int(piecesSplit[1]) - 1)
elif (int(piecesSplit[1]) > 1):
    queen = -(int(piecesSplit[1]) - 1)

if (int(piecesSplit[2]) < 2):
    rooks = abs(int(piecesSplit[2]) - 2)
elif (int(piecesSplit[2]) > 2):
    rooks = -(int(piecesSplit[2]) - 2)

if (int(piecesSplit[3]) < 2):
    bishops = abs(int(piecesSplit[3]) - 2)
elif (int(piecesSplit[3]) > 2):
    bishops = -(int(piecesSplit[3]) - 2)

if (int(piecesSplit[4]) < 2):
    knights = abs(int(piecesSplit[4]) - 2)
elif (int(piecesSplit[4]) > 2):
    knights = -(int(piecesSplit[4]) - 2)

if (int(piecesSplit[5]) < 8):
    pawns = abs(int(piecesSplit[5]) - 8)
elif (int(piecesSplit[5]) > 8):
    pawns = -(int(piecesSplit[4]) - 8)

print(king, queen, rooks, bishops, knights, pawns)
