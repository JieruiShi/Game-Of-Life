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

"""
def stepChange(currentMatrix, staynumber, bornnumber):
    nextMatrix = np.zeros(shape = self.currentMatrix.shape, dtype = bool)
    for i in range(currentMatrix.shape[0]):
        for j in range(currentMatrix.shape[1]):
            if getAdjacent2(i,j) in staynumber:
                nextMatrix[i][j] = currentMatrix[i][j]
            if getAdjacent2(i,j) in bornnumber:
                nextMatrix[i][j] = True
            else:
                nextMatrix[i][j] = False
    return nextMatrix


Matrix1 = GOLMatrix(5,6)
print (Matrix1.currentMatrix)
Matrix1.initialCondition(((1,1),(1,2),(2,2),(3,3)))
print (Matrix1.currentMatrix)
Matrix1.stepChange()
print (Matrix1.currentMatrix)
Matrix1.stepChange()
print (Matrix1.currentMatrix)
"""