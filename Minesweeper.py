import MinesweeperBoard as mb
import UserBoard as ub


class Minesweeper():
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.gameOver = False

        self.gameBoard = mb.MinesweeperBoard(self.rows, self.columns, self.mines)
        self.userBoard = ub.UserBoard(self.rows, self.columns)

    def printBoard(self, board):
        if board == "game":
            board = self.gameBoard
        else:
            board = self.userBoard
            
        columnNumbers = "x, y    "
        spaceLine = "  ----"
        for i in range(0, board.columns):
            columnNumbers += "{}    ".format(i)
            spaceLine += "-----"
        print(columnNumbers)
        print(spaceLine)
        for i in range(0, board.rows):
            row = "{}  | [".format(i)
            for j in range(0, board.columns):
                row += "  {}  ".format(board.board[i][j])
            row += "]"
            print(row)

    def guessMine(self, row, column):
        self.userBoard.guessMine(row, column)
    
    def isGuess(self, row, column):
        return self.userBoard.isGuess(row, column)

    def undoGuess(self, row, column):
        self.userBoard.undo(row, column)
    
    def showCell(self, row, column):
        value = self.gameBoard.showCell(row, column)
        if self.gameBoard.isMine(value):
            self.gameOver = True
        elif self.gameBoard.isEmpty(value):
            cellList = self.gameBoard.getConnectedEmptyCells(row, column)
            for cell in cellList:
                cellValue = self.gameBoard.showCell(cell[0], cell[1])
                self.userBoard.setCell(cell[0], cell[1], cellValue)
        else:
            self.userBoard.setCell(row, column, value)
    
    def boardIsFilled(self):
        i = 0
        filled = True
        while(filled and i < self.userBoard.rows):
            if '?' in self.userBoard.board[i]:
                filled = False
            i += 1
        return filled
    
    def isGameOver(self):
        return self.gameOver

    def isValidRow(self, row):
        return row >= 0 and row < self.rows
    
    def isValidColumn(self, column):
        return column >= 0 and column < self.columns
    
    def isEmptyCell(self, row, column):
        return self.userBoard.isEmpty(row, column)