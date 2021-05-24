import random


class MinesweeperBoard():
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = []

        self.initializeEmptyBoard()
        self.placeMines()
        self.placeClues()

    def initializeEmptyBoard(self):
        for i in range(0, self.rows):
            self.board.append([])
            for j in range(0, self.columns):
                self.board[i].append('-')
    
    def placeMines(self):
        for mine in range(0, self.mines):
            notPlaced = True
            while notPlaced:
                position = []
                position.append(random.choice(range(0, self.rows)))
                position.append(random.choice(range(0, self.columns)))

                if self.isEmpty(self.board[position[0]][position[1]]):
                    self.board[position[0]][position[1]] = '0'
                    notPlaced = False
    
    def placeClues(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if not self.isMine(self.board[i][j]):
                    clue = self.checkSurroundingsForMines(i, j)
                    if clue > 0:
                        self.board[i][j] = str(clue)
    
    def checkSurroundingsForMines(self, row, column):
        surroundingMines = 0

        if row-1 >= 0 and column-1 >= 0:
            if self.isMine(self.topLeftNeighbor(row, column)):
                surroundingMines += 1
        if row-1 >= 0:
            if self.isMine(self.topCenterNeighbor(row, column)):
                surroundingMines += 1
        if row-1 >= 0 and column+1 < self.columns:
            if self.isMine(self.topRightNeighbor(row, column)):
                surroundingMines += 1
        if column-1 >= 0:
            if self.isMine(self.leftNeighbor(row, column)):
                surroundingMines += 1
        if column+1 < self.columns:
            if self.isMine(self.rightNeighbor(row, column)):
                surroundingMines += 1
        if row+1 < self.rows and column-1 >= 0:
            if self.isMine(self.bottomLeftNeighbor(row, column)):
                surroundingMines += 1
        if row+1 < self.rows:
            if self.isMine(self.bottomCenterNeighbor(row, column)):
                surroundingMines += 1
        if row+1 < self.rows and column+1 < self.columns:
            if self.isMine(self.bottomRightNeighbor(row, column)):
                surroundingMines += 1

        return surroundingMines

    def topLeftNeighbor(self, row, column):
        return self.board[row-1][column-1]
    
    def topCenterNeighbor(self, row, column):
        return self.board[row-1][column]
    
    def topRightNeighbor(self, row, column):
        return self.board[row-1][column+1]
    
    def leftNeighbor(self, row, column):
        return self.board[row][column-1]
    
    def rightNeighbor(self, row, column):
        return self.board[row][column+1]
    
    def bottomLeftNeighbor(self, row, column):
        return self.board[row+1][column-1]

    def bottomCenterNeighbor(self, row, column):
        return self.board[row+1][column]
    
    def bottomRightNeighbor(self, row, column):
        return self.board[row+1][column+1]
    
    def isMine(self, cell):
        return cell == '0'
    
    def isEmpty(self, cell):
        return cell == '-'

    def showCell(self, row, column):
        return self.board[row][column]
    
    def getConnectedEmptyCells(self, row, column):
        # Array of cells with their x and y position,
        # as well as a boolean to determine whether they're empty (True)
        # or not (False)
        checked = []
        cells = [[row, column, True]]
        for cell in cells:
            if [cell[0], cell[1]] not in checked and cell[2]:
                if cell[0]-1 >= 0 and cell[1]-1 >= 0:
                    empty = self.isEmpty(self.topLeftNeighbor(cell[0], cell[1]))
                    cells.append([cell[0]-1, cell[1]-1, empty])
                if cell[0]-1 >= 0:
                    empty = self.isEmpty(self.topCenterNeighbor(cell[0], cell[1]))
                    cells.append([cell[0]-1, cell[1], empty])
                if cell[0]-1 >= 0 and cell[1]+1 < self.columns:
                    empty = self.isEmpty(self.topRightNeighbor(cell[0], cell[1]))
                    cells.append([cell[0]-1, cell[1]+1, empty])
                if cell[1]-1 >= 0:
                    empty = self.isEmpty(self.leftNeighbor(cell[0], cell[1]))
                    cells.append([cell[0], cell[1]-1, empty])
                if cell[1]+1 < self.columns:
                    empty = self.isEmpty(self.rightNeighbor(cell[0], cell[1]))
                    cells.append([cell[0], cell[1]+1, empty])
                if cell[0]+1 < self.rows and cell[1]-1 >= 0:
                    empty = self.isEmpty(self.bottomLeftNeighbor(cell[0], cell[1]))
                    cells.append([cell[0]+1, cell[1]-1, empty])
                if cell[0]+1 < self.rows:
                    empty = self.isEmpty(self.bottomCenterNeighbor(cell[0], cell[1]))
                    cells.append([cell[0]+1, cell[1], empty])
                if cell[0]+1 < self.rows and cell[1]+1 < self.columns:
                    empty = self.isEmpty(self.bottomRightNeighbor(cell[0], cell[1]))
                    cells.append([cell[0]+1, cell[1]+1, empty])
                checked.append([cell[0], cell[1]])
        return cells

