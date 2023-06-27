""" This file will contain details about: Sudoku Solver """

def solve_sudoku(sudoku: list[list]) -> list[list]:
   """
   Solves a 9x9 Sudoku by adding in the values
   Note that the values of 0 are the ones to be filled in
   """
   return sudoku

def aes_print(sudoku: list[list[int]]):
    """
    Print a 9x9 Sudoku in a aesthetic way
    """
    horizontal_line = '-------------------------'
    print(horizontal_line)
    for i in range(0, 9):
        for j in range(0, 9, 3):
            if j == 0:
                print("|" + str(sudoku[i][j:j+3])[1:-1], end="|")
            else:
                print(str(sudoku[i][j:j+3])[1:-1], end="|")
        print()
        if (i+1) % 3 == 0:
            print(horizontal_line)


if __name__ == "__main__":
    board = [
    [0, 0, 6, 1, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 4, 0, 0, 0, 3],
    [0, 4, 7, 0, 0, 3, 0, 0, 1],
    [0, 8, 0, 9, 0, 1, 0, 4, 0],
    [0, 0, 4, 0, 0, 0, 3, 0, 0],
    [0, 5, 0, 4, 0, 7, 0, 2, 0],
    [3, 0, 0, 6, 0, 0, 7, 9, 0],
    [6, 0, 0, 0, 8, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 9, 6, 0, 0]]

    solution = [
    [9, 3, 6, 1, 7, 5, 2, 8, 4],
    [2, 1, 5, 8, 4, 6, 9, 7, 3],
    [8, 4, 7, 2, 9, 3, 5, 6, 1],
    [7, 8, 3, 9, 6, 1, 5, 4, 2],
    [5, 9, 4, 7, 2, 8, 3, 1, 6],
    [1, 5, 2, 4, 3, 7, 8, 2, 9],
    [3, 2, 1, 6, 5, 4, 7, 9, 8],
    [6, 7, 9, 3, 8, 2, 1, 4, 5],
    [4, 6, 8, 5, 1, 9, 6, 3, 7]]
    
    aes_print(board)
    #assert(solve_sudoku(board) == solution)