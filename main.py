import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_symbol = 'X'
    ai_symbol = 'O'

    while True:
        print_board(board)

        # Player move
        player_row, player_col = player_move(board)
        board[player_row][player_col] = player_symbol

        # Check if the player wins
        if check_winner(board, player_symbol):
            print_board(board)
            print("Congratulations! You win!")
            break

        # Check if the board is full
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = ai_symbol

        # Check if the AI wins
        if check_winner(board, ai_symbol):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

        # Check if the board is full
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
