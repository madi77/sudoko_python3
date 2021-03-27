### Marinel Dimitrije
myBoard=[0,2,5,7,3,0,0,0,0,
          0,4,0,0,8,5,7,0,0,
          7,8,0,0,0,4,0,0,0,
          4,0,0,9,5,0,0,7,1,
          9,1,7,0,2,0,0,5,3,
          0,0,3,0,1,7,0,4,0,
          0,7,4,5,0,6,1,3,8,
          0,9,0,0,0,1,5,2,0,
          0,0,0,8,0,2,0,6,4] 

# Sudoku-solver takes a list of 81 numbers as input
def solve(sudoku_list):
    myBoard = [sudoku_list[x:x+9] for x in range(0, len(sudoku_list), 9)]
    
    solveBoard(myBoard)
 
    for line in myBoard:
        print(*line)
    
    
    
    
def isValid(board, row, col, num):
 
    #check row
    for i in range(9):
        if board[row][i] == num:
            return False
 
    #check col
    for i in range(9):
        if board[i][col] == num:
            return False
 
    #get top-left corner
    c_row = row - row%3
    c_col = col - col%3
 
    #check 3x3 square
    for i in range(c_row, c_row+3):
        for j in range(c_col, c_col+3):
            if board[i][j] == num:
                return False
 
    #return True if none of the cases above returns False
    return True
 
'''
Define the solveBoard() function,
which solves the Sudoku board using recursion
'''
 
def solveBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if isValid(board, i, j, num):
                        board[i][j] = num
                        result = solveBoard(board)
                        if result == True:
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True
 
### call the function
solve(myBoard)