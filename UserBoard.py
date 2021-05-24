import MinesweeperBoard as mb

class UserBoard():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []

        self.initializeEmptyBoard()
    
    def initializeEmptyBoard(self):
        for i in range(0, self.rows):
            self.board.append([])
            for j in range(0, self.columns):
                self.board[i].append('?')

    def guessMine(self, row, column):
        self.board[row][column] = 'x'
    
    def setCell(self, row, column, value):
        self.board[row][column] = str(value)
    
    def isGuess(self, row, column):
        return self.board[row][column] == 'x'

    def undo(self, row, column):
        self.board[row][column] = '?'

    def isEmpty(self, row, column):
        return self.board[row][column] == '?'