# Juego básico de TicTacToe (consola)
import random

def print_board(b):
    for i in range(0, 9, 3):
        print(" | ".join(b[i:i+3]))
        if i < 6: print("-" * 9)

def check_win(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b_]==b[c]==p for a,b_,c in wins)

def is_full(b):
    return all(c != " " for c in b)

def play():
    board = [" "] * 9
    player = "X"
    while True:
        print_board(board)
        try:
            if player == "O":  # IA simple
                move = random.choice([i for i, v in enumerate(board) if v == " "])
            else:
                move = int(input(f"Turno {player}. Elige casilla (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Movimiento inválido. Intenta otra vez.")
                continue
        except ValueError:
            print("Entrada inválida. Introduce un número 1-9.")
            continue

        board[move] = player
        if check_win(board, player):
            print_board(board)
            print(f"¡Gana {player}!")
            break
        if is_full(board):
            print_board(board)
            print("Empate.")
            break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play()