"""
On défini la logique suivante pour le board:
- 0 la case est jouable (n'appartient à personne)
- 1 elle appartient au joueur ayant commencé là partie
- -1 elle appartient au second joueur
- 2 elle n'est pas jouable
"""
#from copy import deepcopy
from .Data import *
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

    def __init__(self, n):
        self.n = n  # boar de 17x17 pour les "pions"
        self.pawns = [None]*self.n  # On créé les colonnes
        self.areas_b = [None]*self.n # Tableau qui associe les zones aux pions
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
        return self.pawns[index]


    def get_legal_moves(self):
        moves = set()

        for x in range(self.n):
            for y in range(self.n):
                if self.pawns[x][y] == 0:
                    moves.add((x,y))
        return list(moves)

    def has_legal_moves(self):
        #return True if len(self.get_legal_moves()) > 0 else False
        for x in range(self.n):
            for y in range(self.n):
                if self.pawns[x][y] == 0:
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
        assert self[x][y] == 0
        self[x][y] = color


    def __getAreas(self, player):

        p_areas = set()
        for i in range(len(self.areas_dict)):
            count = 0
            for (x,y) in self.areas_dict[i]["pawns"]:
                if self.pawns[x][y] == player:
                    count += 1
            if count >= len(self.areas_dict[i]["pawns"])/2:
                p_areas.add(i-1)
        return list(p_areas)


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


    def hasWon(self, player):
        start = []
        end = []
        player_areas = self.__getAreas(player)

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

