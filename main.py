# This is a sample Python script.


board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def print_board():
    print("|", str(board[0][0]), "|", str(board[0][1]), "|", str(board[0][2]), "|")
    print("|", str(board[1][0]), "|", str(board[1][1]), "|", str(board[1][2]), "|")
    print("|", str(board[2][0]), "|", str(board[2][1]), "|", str(board[2][2]), "|")


board2 = {"1": board[0][0], "2": board[0][1], "3": board[0][1]}

while True:
    col = int(input("Please select the column to put the symbol right there (1,2 or 3): "))
    row = int(input("Please select the row to put the symbol there (1,2 or 3): "))
    board[col][row] = 'O'
    print_board()
