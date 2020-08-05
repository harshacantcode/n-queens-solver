import numpy as np

#A function to find x ** y, time compleity: O(log(y))
def xpowy(x, y):
    retVal = 1
    while(y > 0):
        if(y & 1 == 1):
            retVal = retVal * x
        y = y >> 1
        # Right shifting y
        x = x * x
        # As y has been right shifted, in its binary expansion we're going to the next power of 2
    return retVal

def safeCell(queenOnRow, x, y, board, n):
    if(queenOnRow[x] == 1):
        return False

    #To check if there is a queen present on a diagonal to the proposed grid point.

    ## FOR REFERENCE ##
    # Board numbering is as follows
    # 00 01 02 03 ...
    # 10 11 12 13 ...
    # 20 21 22 23 ...
    # 30 31 32 33 ...
    # .  .  .  .

    #Checking along the North-West diagonal
    iterRow = x
    iterCol = y
    while(iterRow > 0 and iterCol > 0):
        iterRow -= 1
        iterCol -= 1
        if(board[iterRow][iterCol] == 1):
            return False

    #Checking the North-East diagonal
    iterRow = x
    iterCol = y
    while(iterRow > 0 and iterCol + 1 < n):
        iterRow -= 1
        iterCol += 1
        if(board[iterRow][iterCol] == 1):
            return False

    #Checking the South-East diagonal
    iterRow = x
    iterCol = y
    while(iterRow + 1 < n and iterCol + 1 < n):
        iterRow += 1
        iterCol += 1
        if(board[iterRow][iterCol] == 1):
            return False

    #Checking the South-West diagonal
    iterRow = x
    iterCol = y
    while(iterRow + 1 < n and iterCol > 0):
        iterRow += 1
        iterCol -= 1
        if(board[iterRow][iterCol] == 1):
            return False

    return True

def solver(queensPlaced, colNum, queenOnRow, board, n):
    if(queensPlaced == n):
        return True

    for row in range(n):
        if(safeCell(queenOnRow, row, colNum, board, n)):
            board[row][colNum] = 1
            queenOnRow[row] = 1
            queensPlaced += 1
            if(solver(queensPlaced, colNum + 1, queenOnRow, board, n)):
                return True
            else:
                board[row][colNum] = 0
                queenOnRow[row] = 0
                queensPlaced -= 1

    #n queens cannot be placed
    return False

def main():
    n = input("How many Queens? \n")
    n = int(n)
    board = np.zeros(xpowy(n, 2)).reshape(n, n)
    #Creating an nxn grid of zeros on which we have to place n queens
    queensPlaced = 0
    queenOnRow = np.zeros(n)

    if(solver(queensPlaced, 0, queenOnRow, board, n)):
        print(board)
        #We can observe that a solution exists for all natural numbers
        #apart from 2 and 4.
    else:
        print("There is no possible configuration :(")
main()
