from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .ConhexLogic import Board
import numpy as np

class ConHexGame(Game):

    def __init__(self, n):
        self.n = n

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pawns)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.n)

    def getActionSize(self):
        # return number of actions
        #return sum(len(x) for x in Board.playable)
        return self.n*self.n + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.n*self.n:
            return (board, -player)
        b = Board(self.n)
        b.pawns = np.copy(board)
        move = (int(action/self.n), action%self.n)
        b.execute_move(move, player)
        return (b.pawns, -player)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pawns = np.copy(board)
        legalMoves =  b.get_legal_moves()
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.n*x+y]=1
        return np.array(valids)


    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pawns = np.copy(board)
        start = list()
        end = list()
        player_areas = list()
        if b.has_legal_moves():
            if b.hasWon(player):
                return player
            elif b.hasWon(-player):
                return -player
            else:
                return 0

        return 0.000001

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player*board

    def getSymmetries(self, board, pi):
        # mirror, rotational
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

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    def display(self,board):
        board.debug()

    def getScore(self, board, player):
        b = Board(self.n)
        b.panws = np.copy(board)
        score = 0

        if player == 1:
            score = len(b.red)
        else:
            score = len(b.blue)
        return score




#a=ConHexGame(17)
#print(a.getActionSize())
