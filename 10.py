# Python program to solve N Queen problem

N = 4  # Size of the chessboard (4x4)

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # Base case: If all queens are placed, then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, 
            # then backtrack: remove queen from board[i][col]
            board[i][col] = 0

    return False

def solveNQ():
    # Initialize the board with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Call the utility function to solve the problem
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    # If a solution is found, print it
    printSolution(board)
    return True

# Driver program to test above function
solveNQ()
