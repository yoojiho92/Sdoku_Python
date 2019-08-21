import math
import random



def findNextCellToFill(grid, i, j, n):
        for x in range(i,n):
                for y in range(j,n):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,n):
                for y in range(0,n):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e, n):
        nm = int(math.sqrt(n));
        rowOk = all([e != grid[i][x] for x in range(n)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(n)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = nm *(i//nm), nm *(j//nm) #floored quotient should be used here.
                        for x in range(secTopX, secTopX+nm):
                                for y in range(secTopY, secTopY+nm):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        n = len(grid)
        i,j = findNextCellToFill(grid, i, j, n)
        if i == -1:
                return True
        for e in range(1,1+n):
                if isValid(grid,i,j,e,n):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

        def makeRandomGrid(n):
        grid = []
        grid2 = []
        for i in range(0,n):
            for j in range(0,n):
                if i == 0:
                    grid2.append(j+1)
                    random.shuffle(grid2)
                else:
                    grid2.append(0)
            grid.append(grid2)
            grid2 = []


        return grid
grid = makeRandomGrid(4)
solveSudoku(grid)
print(grid)


#print("----")
#print(solveSudoku(input2))
#print(input3)
