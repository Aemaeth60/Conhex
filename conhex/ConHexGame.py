from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .ConhexLogic import Board
import numpy as np

class ConHexGame(Game):

    def __init__(self):
        self.width = 10
        self.height = 11

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board()
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.width, self.height)

    def getActionSize(self):
        # return number of actions
        #return sum(len(x) for x in Board.playable) +1
        return self.width*self.height# + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.width*self.height:
            return (board, -player)
        b = Board()
        b.pieces = np.copy(board)
        move = (int(action/self.width), action%self.width)

        b.execute_move(move, player)

        return (b.pieces, -player)


    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board()
        b.pieces = np.copy(board)
        #print(board)
        legalMoves =  b.get_legal_moves()
        #print(legalMoves)
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.width*x+y]=1
        return np.array(valids)


    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board()
        b.pieces = np.copy(board)

        r_won = b.hasWon(1)
        b_won = b.hasWon(-1)


        if r_won:
            return 1
        elif b_won:
            return -1
 
        return 0

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player*board

    def getSymmetries(self, board, pi):
        # mirror, rotational
        """
        assert(len(pi) == self.n**2+1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l
        """
        return [(board,pi)]

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    def getScore(self, board, player):
        b = Board(self.n, self.width, self.height)
        b.pieces = np.copy(board)
        score = 0

        if player == 1:
            score = len(self.r_areas)
        else:
            score = len(self.b_areas)
        return score


def display(board):
    #board.debug()
    #n = board.shape[0]
    #b = Board(n)
    #b.pawns = np.copy(board)


    #print("Areas player red : ", b.r_areas)
    #print("Areas player blue : ", b.b_areas)
    for y in range(10):
        print (y,"|",end="")
    print("")
    print(" -----------------------")
    for y in range(11):
        print(y, "|",end="")    # print the row #
        for x in range(10):
            piece = board[y][x]    # get the piece to print
            if piece == -1: print("b ",end="")
            elif piece == 1: print("r ",end="")
            else:
                if x==10:
                    print("-",end="")
                else:
                    print("- ",end="")
        print("|")

    print("   -----------------------")


