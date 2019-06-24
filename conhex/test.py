import keyboard
from datetime import datetime
from ConhexLogic import Board

i = 0
b = Board(17)
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