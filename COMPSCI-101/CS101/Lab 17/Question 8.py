board = [["O", "X", " "],["O", "X", " "],["O", " ", " "]]
def print_board(board):
    for i in range(3):
        print('|'.join(board[i]))
        if i < 2:
            print("-----")
print_board(board)