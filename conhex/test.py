import keyboard
from datetime import datetime
from ConhexLogic import Board

i = 0
b = Board(17)

print(b.hasWon(1, [1  ,3,  9, 10, 15, 16, 20, 21, 22, 23, 25, 31, 32, 33, 34, 38, 39]))
print(b.hasWon(-1, [1  ,3,  9, 10, 15, 16, 20, 21, 22, 23, 25, 31, 32, 33, 34, 38, 39]))
print(b.hasWon(1, [5,  8, 14, 17, 18, 26, 27, 28, 29, 30 ,35, 36, 40, 41]))
print(b.hasWon(-1, [5,  8, 14, 17, 18, 26, 27, 28, 29, 30 ,35, 36, 40, 41]))

"""
t = datetime.now()
while i < len(b.areas_dict):
    while not(keyboard.is_pressed('q')) or (datetime.now()-t).seconds < 1:
        continue
    t = datetime.now()
    print()
    print("   ", end="")
    for y in range(17):
        print (y,"|",end="")
    print("")
    print(" -----------------------")
    for y in range(17):
        print(y, "|",end="")    # print the row #
        for x in range(17):
            piece = b.pawns[y][x]    # get the piece to print
            if (y,x) in b.areas_dict[i]["pawns"]:
                print("*", end="")
            #    if piece == 0:
            #        print("*",end="")
            else:
                if x==17:
                    print("-",end=" ")
                else:
                    print("- ",end=" ")
        print("|")

    print("   -----------------------")
    i +=1
"""