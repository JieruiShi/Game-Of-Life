import numpy as np
import pygame

# a class for the special matrix so to put all the functions within the class
class GOLMatrix:
    def __init__(self, rowNumber, columnNumber, staynumber = [2], bornnumber = [3], periodic = False):
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.staynumber = staynumber
        self.bornnumber = bornnumber
        self.periodic = periodic
        self.currentMatrix = np.zeros(shape = (rowNumber,columnNumber), dtype = bool)

    def getAdjacent(self, x, y):
        count = 0
        class outOfBounds(Exception):
            pass
        try:
            for i in [x - 1, x, x + 1]:
                for j in [y - 1, y, y + 1]:
                    if i < 0 or i >= self.currentMatrix.shape[0] or j < 0 or j >= self.currentMatrix.shape[1]:
                        raise outOfBounds
                    else:
                        count += int(self.currentMatrix[i][j])
            count -= self.currentMatrix[x][y]
        except outOfBounds:
            count = 0
        return count

    def stepChange(self):
        nextMatrix = np.zeros(shape = self.currentMatrix.shape, dtype = bool)
        for i in range(self.currentMatrix.shape[0]):
            for j in range(self.currentMatrix.shape[1]):
                if self.getAdjacent(i, j) in self.staynumber:
                    nextMatrix[i][j] = self.currentMatrix[i][j]
                elif self.getAdjacent(i, j) in self.bornnumber:
                    nextMatrix[i][j] = True
                else:
                    nextMatrix[i][j] = False
        self.currentMatrix = nextMatrix

    def initialCondition(self, collection):
        self.currentMatrix = np.zeros(shape = (self.rowNumber,self.columnNumber), dtype = bool)
        for coordinates in collection:
            if len(coordinates) == 2:
                try:
                    self.currentMatrix[coordinates[1]][coordinates[0]] = True
                except:
                    pass

    def display(self, screen, origin, cellDimension, colour = (255,255,255), thickness = 1):
        """Block dimension is the size of each cell. For example a cell with width 5 and height 6 would have cellDimension(5,6),
        thickness is for some space between, to distinguish and for putting grids. Usually, the cell is smaller than the grid dimension
        by thickness."""
        for i in range(self.currentMatrix.shape[0]):
            for j in range(self.currentMatrix.shape[1]):
                if self.currentMatrix[i][j] == True:
                    pygame.draw.rect(screen, colour, (origin[0] + thickness + (cellDimension[0] + thickness)* j, origin[1] + thickness + (cellDimension[1] + thickness) * i, cellDimension[0], cellDimension[1]))

    def centralize(self):
        """shift all the cells to centre. Do this using the furthest point as reference to the edges. Choose right bottom if cannot be exact centre."""
        leftBound = 0
        leftFound = False
        rightBound = self.columnNumber - 1
        rightFound = False
        upperBound = 0
        upperFound = False
        lowerBound = self.columnNumber - 1
        lowerFound = False
        while leftFound == False and leftBound != self.columnNumber:
            if True in newMatrix.currentMatrix[:, leftBound]:
                leftFound = True
            else:
                leftBound += 1
        if leftBound == self.columnNumber:
            pass
        else:
            while rightFound == False:
                if True in newMatrix.currentMatrix[:, rightBound]:
                    rightFound = True
                else:
                    rightBound -= 1

            while upperFound == False:
                if True in newMatrix.currentMatrix[upperBound,:]:
                    upperFound = True
                else:
                    upperBound += 1

            while lowerFound == False:
                if True in newMatrix.currentMatrix[lowerBound,:]:
                    lowerFound = True
                else:
                    lowerBound -= 1
            #calculate difference between centre of True blocks and centre of matrix. Floor divide by 2 together to avoid accumulation of errors.
            leftShift = (leftBound + rightBound + 1 - self.columnNumber)//2
            upShift = (upperBound + lowerBound + 1 - self.rowNumber)//2
            nextMatrix = np.zeros(shape = (self.rowNumber,self.columnNumber), dtype = bool)
            for i in range(nextMatrix.shape[0]):
                for j in range(nextMatrix.shape[1]):
                    try:
                        nextMatrix[i][j] = self.currentMatrix[i + upShift][j + leftShift]
                    except IndexError:
                        pass
            self.currentMatrix = nextMatrix