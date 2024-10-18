import random

def initialize(size):
    game_state = dict()
    for i in range(1, size + 1):
        game_state[i] = dict().fromkeys(range(1, size + 1), " ")
    return game_state

def display_Layout(board):
    for i in range(1, len(board) + 1):
        row_elements = []
        for j in range(1, len(board.get(i)) + 1):
            row_elements.append(board.get(i).get(j))
        print(" | ".join(row_elements))
        print("-" * (4 * len(board)))

def mark_board(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = "X" if player == 1 else "O"
        return True
    else:
        print("The spot is already taken! Try again.")
        return False

def check_winner(board, player):
    Sign = "X" if player == 1 else "O"
    size = len(board)

    # Check rows
    for i in range(1, size + 1):
        if all(board[i][j] == Sign for j in range(1, size + 1)):
            return True

    # Check columns
    for i in range(1, size + 1):
        if all(board[j][i] == Sign for j in range(1, size + 1)):
            return True

    # Check diagonals
    if all(board[i][i] == Sign for i in range(1, size + 1)) or \
       all(board[i][size - i + 1] == Sign for i in range(1, size + 1)):
        return True

    return False

def check_draw(board):
    return all(cell != " " for row in board.values() for cell in row.values())

def alternative_chance(num, board, size):
    while True:
        ip = input(f"Player {num}, enter the row and column (format: row,col): ")
        parts = ip.split(",")
        
        if len(parts) == 2:
            row, col = parts[0], parts[1]

            if row.isdigit() and col.isdigit():
                row, col = int(row), int(col)

                if 1 <= row <= size and 1 <= col <= size:
                    if mark_board(board, num, row, col):
                        break
                    else:
                        print("Invalid move! The position is already occupied.")
                else:
                    print("Invalid input! Row and column must be within the board size.")
            else:
                print("Invalid input! Please enter numbers in the format: row,col.")
        else:
            print("Invalid format! Please enter in the format: row,col.")

def main():
    size = int(input("Enter the Size Of Tic-Tac-Toe: "))
    board = initialize(size)
    display_Layout(board)

    print("Player 1 has X")
    print("Player 2 has O")

    chance = random.randint(1, 2)
    print(f"Chance is of Player {chance}")

    moves_made = 0

    for _ in range(size * size):  
        alternative_chance(chance, board, size)
        display_Layout(board)

        moves_made += 1  

        if moves_made >= 5 and check_winner(board, chance):
            print(f"Player {chance} wins!")
            break

        if moves_made == size * size and check_draw(board):
            print("It's a draw!")
            break

        chance = 1 if chance == 2 else 2

# Call the main function
if __name__ == "__main__":
    main()

