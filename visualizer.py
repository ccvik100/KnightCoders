# visualizer.py – Vizualizáció

from board import ACTIVE_START

def print_board(board, path):
    """
    Kirajzolja a 4x4 aktív táblát a lépéssorrenddel.
    """
    display = [['.' for _ in range(4)] for _ in range(4)]
    for idx, (x, y) in enumerate(path):
        display[x - ACTIVE_START][y - ACTIVE_START] = str(idx)
    for row in display:
        print(' '.join(row))