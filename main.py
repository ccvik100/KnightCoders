# main.py – Projektmenedzseri főprogram

from board import create_board, ACTIVE_START
from solver import dfs
from visualizer import print_board

def main():
    print("=== Éhes huszár – útkereső program ===\n")

    # Tábla létrehozása
    board = create_board()
    start_x, start_y = ACTIVE_START, ACTIVE_START
    board[start_x][start_y] = 1

    # Útvonal tárolása
    path = [(start_x, start_y)]

    # Keresés indítása
    if dfs(board, path, start_x, start_y):
        print("✅ Megoldás találva! Lépéssor:")
        print_board(board, path)
    else:
        print("❌ Nincs megoldás.")

if __name__ == "__main__":
    main()
