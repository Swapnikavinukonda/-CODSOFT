import sys

X = 'X'
O = 'O'
NULL = ' '

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

def is_full(board):
    for row in board:
        for cell in row:
            if cell == NULL:
                return False
    return True

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == NULL]

# Minimax function
def minimax(board, depth, maximizing_player):
    if check_winner(board, X):
        return 10 - depth
    elif check_winner(board, O):
        return -10 + depth
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = -sys.maxsize
        for i, j in get_empty_cells(board):
            board[i][j] = X
            eval = minimax(board, depth + 1, False)
            board[i][j] = NULL
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for i, j in get_empty_cells(board):
            board[i][j] = O
            eval = minimax(board, depth + 1, True)
            board[i][j] = NULL
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using Minimax
def find_best_move(board):
    best_move = None
    best_eval = -sys.maxsize
    for i, j in get_empty_cells(board):
        board[i][j] = X
        eval = minimax(board, 0, False)
        board[i][j] = NULL
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

# Main function to win game
def main():
    board = [[NULL,NULL,NULL],
             [NULL,NULL,NULL],
             [NULL,NULL,NULL]]

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player_move = input("Enter your move (row col): ").split()
        row, col = int(player_move[0]) - 1, int(player_move[1]) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move! Row and column numbers must be between 1 and 3. Try again.")
            continue
        if board[row][col] == NULL:
            board[row][col] = O
        else:
            print("Invalid move! Try again.")
            continue

        if check_winner(board, O):
            print_board(board)
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = X

        if check_winner(board, X):
            print_board(board)
            print("AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
