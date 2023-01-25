# This is a sample Python script

class Otions():
    def __init__(self, lenght):
        self.lenght = lenght

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
    ]


def print_board():
    print("|", str(board[0][0]), "|", str(board[0][1]), "|", str(board[0][2]), "|")
    print("|", str(board[1][0]), "|", str(board[1][1]), "|", str(board[1][2]), "|")
    print("|", str(board[2][0]), "|", str(board[2][1]), "|", str(board[2][2]), "|")

def game():
    global turn
    col = int(input("Please select the column to put the symbol right there (1,2 or 3): "))
    row = int(input("Please select the row to put the symbol there (1,2 or 3): "))
    if board[col][row] is None:
        board[col][row] = player[turn]
        print_board()
        turn = 1 - turn
    else:
        print('The field is already taken! Please select empty field')

player = ["O","X"]
turn = 0
while True:
    game()









