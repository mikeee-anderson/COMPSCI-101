board = [["O", "X", " "],["O", "X", " "],["O", " ", " "]]
def print_board(board):
    for i in range(3):
        print('|'.join(board[i]))
        if i < 2:
            print("-----")

def check_win(board, player):
    # Check rows for win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check main diagonal for win
    if all(board[i][i] == player for i in range(3)):
        return True

    # Check anti-diagonal for win
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    # If no win conditions are met, return False
    return False



print_board(board)
print()
player1, player2 = "O", "X"
print(f"Player {player1} has won? {check_win(board, player1)}")
print(f"Player {player2} has won? {check_win(board, player2)}")