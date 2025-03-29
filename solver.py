# solver.py – Algoritmusfejlesztés

KNIGHT_MOVES = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

from board import is_valid_move, ACTIVE_END

def get_valid_moves(x, y, board):
    valid_moves = []
    for dx, dy in KNIGHT_MOVES:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, board):
            valid_moves.append((nx, ny))
    return valid_moves

def dfs(board, path, x, y):
    if (x, y) == (ACTIVE_END, ACTIVE_END):
        return True

    for nx, ny in get_valid_moves(x, y, board):
        board[nx][ny] = 1
        path.append((nx, ny))
        if dfs(board, path, nx, ny):
            return True
        path.pop()
        board[nx][ny] = 0

    return False
