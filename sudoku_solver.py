""" This file will contain details about: Sudoku Solver """

def solve_sudoku(sudoku: list[list[int]]) -> list[list[int]]:
    """
    Solves a 9x9 Sudoku by adding in the values
    Note that the values of 0 are the ones to be filled in
    It will use a brute force or backtracking approach
    Essentially, numbers cannot repeat in a row, column or 3x3 subgrid.
    Returns a solved sudoku
    """
    if is_complete(sudoku): #If sudoku is completed, return it
        return sudoku
   
    row, column = find_empty_cell(sudoku) #Find an available row column (i.e a cell with an entry of 0)

    for k in range(1, 10):
        if is_valid(sudoku, row, column, k):
            sudoku[row][column]= k 

            if solve_sudoku(sudoku): #Keep solving the sudoku, assuming the above is selected in correct spot
                return sudoku
            
            sudoku[row][column] = 0 #If a sudoku is not returned by then, it is not valid, reset relevant cells to 0
       
    return None

def find_empty_cell(sudoku: list[list[int]]):
    """
    Finds an empty cell within the sudoku
    Does not worry about invalid inputs as we will check before hand in solve_sudoku
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
            
def is_complete(sudoku: list[list[int]]) -> bool:
    """
    Checks whether the sudoku has been solved or not
    O(1)
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

def is_valid(sudoku: list[list[int]], row: int, column: int, value: int) -> bool:
    """
    Checks whether a value can be added in sudoku[row][column]
    """
    res_row = value not in sudoku[row]
    res_column = value not in [sudoku[i][column] for i in range(9)]

    start_row = (row // 3) * 3
    start_column = (column // 3) * 3
    res_grid = value not in [sudoku[i][j] for i in range(start_row, start_row+3) for j in range(start_column, start_column+3)] #Find all the values in the grid
    return res_row and res_column and res_grid #If any is False, we cannot select the row/column


def aes_print(sudoku: list[list[int]]):
    """
    Print a 9x9 Sudoku in an aesthetic manner
    """
    horizontal_line = '-------------------------'
    print(horizontal_line)
    for i in range(9):
        for j in range(0, 9, 3):
            if j == 0:
                print("|" + str(sudoku[i][j:j+3])[1:-1], end="|")
            else:
                print(str(sudoku[i][j:j+3])[1:-1], end="|")
        print()
        if (i+1) % 3 == 0:
            print(horizontal_line)


if __name__ == "__main__":
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    
    solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    aes_print(solve_sudoku(board))

