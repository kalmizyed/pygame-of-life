import random
import numpy

class Board:
    def __init__(self, width, height, size, rule, seed_size):
        self.size = size
        dim = self.asBoardPos((width, height))
        self.board = numpy.empty(dim)
        self.board.fill(0)
        self.width = dim[0]
        self.height = dim[1]
        self.rule = rule
        self.seed_size = seed_size
        self.mouseHistory = set()
    
    def liveNeighbors(self, pos):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                sum += self.board[(pos[0]+j) % self.width, (pos[1]+i) % self.height]
        return sum
    
    def update(self):
        newBoard = numpy.empty((self.width, self.height))
        newBoard.fill(0)
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.liveNeighbors((col, row))
                if self.board[col, row] == 0:
                    if neighbors in self.rule['b']:
                        newBoard[col, row] = 1
                else:
                    if neighbors in self.rule['s']:
                        newBoard[col, row] = 1
        self.board = newBoard

    def initialize(self):
        random.seed()
        for row in range(self.height//self.seed_size//2, 3*self.height//self.seed_size//2):
            for col in range(self.width//self.seed_size//2, 3*self.width//self.seed_size//2):
                self.board[col, row] = int(max(random.uniform(-5, 2), 0))
    
    def clear(self):
        self.board.fill(0)
    
    def handleMouse(self, pos):
        pos = self.asBoardPos(pos)
        if pos in self.mouseHistory:
            return
        else:
            self.flipPixel(pos)
            self.mouseHistory.add(pos)
    
    def clearMouseHistory(self):
        self.mouseHistory = set()

    def flipPixel(self, pos):
        self.board[pos] = 0 if self.board[pos] == 1 else 1

    def asBoardPos(self, pos):
        return tuple(int(coord/self.size) for coord in pos)