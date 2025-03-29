# board.py – Tábla logika és mozgáskezelés

BOARD_SIZE = 8
ACTIVE_START = 2
ACTIVE_END = 5

def create_board():
    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for i in range(ACTIVE_START, ACTIVE_END + 1):
        for j in range(ACTIVE_START, ACTIVE_END + 1):
            board[i][j] = 0
    return board

def is_valid_move(x, y, board):
    return ACTIVE_START <= x <= ACTIVE_END and ACTIVE_START <= y <= ACTIVE_END and board[x][y] == 0

