"""
On défini la logique suivante pour le board:
- 0 la case est jouable (n'appartient à personne)
- 1 elle appartient au joueur ayant commencé là partie
- -1 elle appartient au second joueur
- 2 elle n'est pas jouable
"""
#from copy import deepcopy
from .Data import *
import math
import numpy as np
#import sys
#sys.setrecursionlimit(10000)

class Board():

    r_start_areas = [1, 6, 17, 28, 37]
    r_end_areas = [5, 11, 24, 36, 41]
    b_start_areas = [37, 38, 39, 40, 41]
    b_end_areas = [1, 2, 3, 4, 5]

    #Tableau de dict composé de {voisines: [aires voisines], pions: [(tuple)}

    playable = [
        [0, 16],
        [2, 4, 6, 8, 10, 12, 14],
        [1, 15],
        [4, 6, 8, 10, 12],
        [1, 3, 13, 15],
        [6, 8, 10],
        [1, 3, 5, 11, 13, 15],
        [8],
        [1, 3, 5, 7, 8, 9, 11, 13, 15]
    ]

    playable2 = [
        [0, 16],
        [2, 4, 6, 8, 10, 12, 14],
        [1, 15],
        [4, 6, 8, 10, 12],
        [1, 3, 13, 15],
        [6, 8, 10],
        [1, 3, 5, 11, 13, 15],
        [8],
        [1, 3, 5, 7, 8, 9, 11, 13, 15],
        [8],
        [1, 3, 5, 11, 13, 15],
        [6, 8, 10],
        [1, 3, 13, 15],
        [4, 6, 8, 10, 12],
        [1, 15],
        [2, 4, 6, 8, 10, 12, 14],
        [0, 16]
    ]

    areas = pawns_places

    """
    areas_weights = [
        3, 3, 3, 3, 3,
        3, 6, 6, 6, 6, 3,
        6, 6, 6, 6, 6,
        3, 6, 6, 6, 6, 6, 6, 3,
        4,
        6, 6, 3,
        6, 6, 6, 6, 6, 6, 6, 3,
        3, 3, 3, 3, 3
    ]
    """

    def __init__(self, n, width, height):
        self.n = n  # boar de 17x17 pour les "pions"
        self.width = width
        self.height = height
        self.pawns = [None]*self.n  # On créé les colonnes
        self.areas_b = [None]*self.n # Tableau qui associe les zones aux pions
        self.pieces = [None]*self.height

        for i in range(len(self.pieces)):
            self.pieces[i] = [0]*self.width
        #Tableau qui stocke les pions détenu par un joueur
        #self.red = []  # 1
        #self.blue = []  # -1
        self.areas_dict = areas_dict

        #On rempli toutes les cases à 2 (non jouable)
        for i in range(self.n):
            self.pawns[i] = [2]*self.n
            self.areas_b[i] = [2]*self.n

        #On rempli les 7 premières lignes
        for i in range(int(self.n/2)):
            for idx in self.playable[i]:
                self.pawns[i][idx] = 0
                self.areas_b[i][idx] = 0
            self.pawns[int(self.n)-i-1] = self.pawns[i][:]
            self.areas_b[int(self.n)-i-1] = self.pawns[i][:] # on rempli les 7 autres lignes par symétrie

        #On rempli la ligne du milieu
        for idx in self.playable[8]:
            self.pawns[8][idx] = 0
            self.areas_b[8][idx] = 0


        #self.areas_b = deepcopy(self.pawns)

        it = iter(self.areas)
        for x in self.areas_b:
            for i in range(len(x)):
                if x[i] == 0:
                    x[i] = next(it)


    def __getitem__(self, index):
        return self.pieces[index]


    def get_legal_moves(self):
        moves = set()

        for x in range(self.width):
            for y in range(self.height):
                if self.pieces[y][x] == 0:
                    moves.add((y,x))
        return list(moves)

    def has_legal_moves(self):
        #return True if len(self.get_legal_moves()) > 0 else False
        for x in range(self.height):
            for y in range(self.width):
                if self.pieces[x][y] == 0:
                    return True
        return False


    def execute_move(self, move, color):
        """Perform the given move on the board; flips pieces as necessary.
        color gives the color pf the piece to play (1=white,-1=black)
        """

        #Much like move generation, start at the new piece's square and
        #follow it on all 8 directions to look for a piece allowing flipping.

        # Add the piece to the empty square.
        # print(move)
        (x, y) = move
        #assert self[x][y] == 0
        if(self[x][y] != 0):
            print("Erreur aux coordonnées : ", x, y)
            raise AssertionError()
            
        self[x][y] = color
        self.fillPawns()

    def fillPawns(self):

        i = 0
        for y in range(len(self.playable2)):
            for x in self.playable2[y]:
                self.pawns[y][x] = self.pieces[int(i/self.width)][i%self.width]
                i +=1


    def getAreas(self, red, blue):

        p_areas_red = set()
        p_areas_blue = set()
        """
        canonical = False
        a = [(x,y) for x,y in zip (range(self.n), range(self.n))]
        for x,y in a:
            if self.pawns[x][y] ==2:
                break
            elif self.pawns[x][y] == -2:
                canonical = True
                break
        """


        for i in range(len(self.areas_dict)):
            count_red = 0
            count_blue = 0
            if int(i+1) in red or int(i+1) in blue:
                continue
            for (x,y) in self.areas_dict[i]["pawns"]:
                if False:
                    if self.pawns[x][y] == -1:
                        count_red +=1
                    elif self.pawns[x][y] == 1:
                        count_blue +=1
                else:
                    if self.pawns[x][y] == 1:
                        count_red +=1
                    elif self.pawns[x][y] == -1:
                        count_blue +=1
            if count_red >= math.ceil(len(self.areas_dict[i]["pawns"])/2.0):
                p_areas_red.add(i+1)
            elif count_blue >= math.ceil(len(self.areas_dict[i]["pawns"])/2.0):
                p_areas_blue.add(i+1)
        p_areas_red = list(p_areas_red)
        p_areas_blue = list(p_areas_blue)
        p_areas_red.extend(red)
        p_areas_blue.extend(blue)
        p_areas_red = list(sorted(set(p_areas_red)))
        p_areas_blue = list(sorted(set(p_areas_blue)))
        return p_areas_red, p_areas_blue
    """
    def getAreas(self, player, player_areas, opponent):
        p_areas = set()
        canonical = False
        curP = np.copy(player_areas)
        oppP = np.copy(opponent)
        a = [(x,y) for x,y in zip (range(self.n), range(self.n))]
        for x,y in a:
            if self.pawns[x][y] ==2:
                break
            else:
                canonical = True
                curP = np.copy(opponent)
                oppP = np.copy(player_areas)
                break


        for i in range(len(self.areas_dict)):
            count = 0
            if int(i+1) in curP or int(i+1) in oppP:
                continue
            for (x,y) in self.areas_dict[i]["pawns"]:
                if self.pawns[x][y] == player and canonical == False:
                    count += 1
                elif self.pawns[x][y] == -player and canonical == True:
                    count += 1
            if count >= math.ceil(len(self.areas_dict[i]["pawns"])/2.0):
                p_areas.add(i+1)
        p_areas = list(p_areas)
        p_areas.extend(curP)
        p_areas = list(sorted(set(p_areas)))
        return p_areas
        """

    def __areaRec(self, area, end , player_areas, visited):
        visited.append(area)
        if area in player_areas:
            if area in end:
                return True
            else:
                ret = False
                for i in self.areas_dict[int(area)-1]["neighbors"]:
                    if i not in visited:
                        temp_ret = self.__areaRec(i, end, player_areas,visited)
                        ret = ret | temp_ret
                return ret
        return False
    #list(set(board.areas_dict[int(area)-1]["neighbors"]) & set(player_areas))


    def hasWon(self, player, player_areas):
        start = []
        end = []
        #player_areas = self.getAreas(player, [], [])
        if player == 1:
            start = self.r_start_areas
            end = self.r_end_areas
        else:
            start = self.b_start_areas
            end = self.b_end_areas

        #display(board.pawns)
        #print(player_areas, player)

        ret = False
        for area in start:
            ret |= self.__areaRec(area, end, player_areas, [])
        return ret


    def debug(self):
        for tab in self.pawns:
            print(tab)
        for tab in self.areas_b:
            print(tab)

"""
a = Board(17)
a.debug()
print(a.get_legal_moves())
"""

