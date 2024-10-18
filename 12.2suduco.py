import random
import math

def initialize():
    size = int(input("Enter the size (e.g., 3 for 3x3, 4 for 4x4): "))
    grid = create_puzzle(size)
    return grid, size

def create_puzzle(size):
    grid = [[0] * size for _ in range(size)]
    fill_grid(grid, size)
    return grid

def fill_grid(grid, size):
    for r in range(size):
        nums = list(range(1, size + 1))
        random.shuffle(nums)
        for c in range(size):
            grid[r][c] = nums[c]

    for c in range(size):
        col_set = set()
        for r in range(size):
            while grid[r][c] in col_set:
                grid[r][c] = random.randint(1, size)
            col_set.add(grid[r][c])

def display_layout(board):
    size = len(board)
    horizontal_border = "-" * (4 * size + 1)
    
    print(horizontal_border)
    for i in range(size):
        row_elem = ["|"]
        for j in range(size):
            row_elem.append(str(board[i][j]))
            row_elem.append("|")
        print(" ".join(row_elem))
        print(horizontal_border)

def start_game(size, grid):
    difficulty_level = input("Enter Difficulty level (For Ex: Easy, Medium, Hard): ")
    print("Setting the Game for You: All the Best")
    remove_elements_from_grid(difficulty_level, size, grid)

def remove_elements_from_grid(diff_level, size, grid):
    no_of_elements_to_remove = 0
    if diff_level in ['Easy', 'easy']:
        no_of_elements_to_remove = math.ceil(0.25 * (size * size))
    elif diff_level in ['Medium', 'medium']:
        no_of_elements_to_remove = math.ceil(0.50 * (size * size))
    elif diff_level in ['Hard', 'hard']:
        no_of_elements_to_remove = math.ceil(0.75 * (size * size))

    removed_count = 0
    
    while removed_count < no_of_elements_to_remove:
        row = random.randint(0, size - 1)
        column = random.randint(0, size - 1)
        
        if grid[row][column] != ' ':
            grid[row][column] = ' '
            removed_count += 1

    display_layout(grid)

def user_input(size, grid):
    print("Enter your numbers in the following format: row column number (e.g., 0 1 5 to place 5 in row 0 column 1)")
    while True:
        try:
            row, col, number = map(int, input("Enter row, column and number (or -1 to finish): ").split())
            if row == -1:
                break
            if grid[row][col] == ' ':
                grid[row][col] = number
                display_layout(grid)
            else:
                print("You can only override empty spaces.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row, column, and number.")

def is_valid_sudoku(grid):
    size = len(grid)
    for i in range(size):
        if len(set(grid[i])) != len([x for x in grid[i] if x != ' ']):
            return False
        column = [grid[r][i] for r in range(size)]
        if len(set(column)) != len([x for x in column if x != ' ']):
            return False
            
    square_size = int(math.sqrt(size))
    for i in range(0, size, square_size):
        for j in range(0, size, square_size):
            square_set = set()
            for r in range(square_size):
                for c in range(square_size):
                    num = grid[i + r][j + c]
                    if num != ' ':
                        if num in square_set:
                            return False
                        square_set.add(num)
    
    return True

def end_game(grid):
    if is_valid_sudoku(grid):
        print("Congratulations! You've completed the Sudoku successfully!")
    else:
        print("Game over. The Sudoku is not valid.")

def sudoku():
    board, size = initialize()
    display_layout(board)
    start_game(size, board)
    user_input(size, board)
    end_game(board)

sudoku()

