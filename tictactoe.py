
import random
import time

score = {"Wins": 0, "Losses": 0, "Draws": 0}

def clear_screen():
    print("\033[H\033[J", end="")  # ANSI escape to clear terminal

def print_score():
    print("=" * 35)
    print(f"  Wins: {score['Wins']}  |  Losses: {score['Losses']}  |  Draws: {score['Draws']}")
    print("=" * 35)

def print_board(board):
    symbols = {0: " ", 1: "X", 2: "O"}
    print("\n")
    for i in range(3):
        row = ""
        for j in range(3):
            cell = symbols[board[i][j]]
            row += f"  {cell}  "
            if j < 2:
                row += "│"
        print(row)
        if i < 2:
            print("─────┼─────┼─────")
    print("\n")

def print_positions():
    """Show available position numbers for player reference."""
    print("  Position map:")
    num = 1
    for i in range(3):
        row = ""
        for j in range(3):
            row += f"  {num}  "
            if j < 2:
                row += "│"
            num += 1
        print(row)
        if i < 2:
            print("─────┼─────┼─────")
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != 0 for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def minimax(board, is_maximizing):
    if check_winner(board, 2):
        return 10
    if check_winner(board, 1):
        return -10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -100
        for i, j in get_empty_cells(board):
            board[i][j] = 2
            best = max(best, minimax(board, False))
            board[i][j] = 0
        return best
    else:
        best = 100
        for i, j in get_empty_cells(board):
            board[i][j] = 1
            best = min(best, minimax(board, True))
            board[i][j] = 0
        return best

def computer_move(board):
    empty = get_empty_cells(board)
    # 35% optimal, 65% random
    if random.random() < 0.35:
        return get_best_move(board)
    return random.choice(empty)

def get_best_move(board):
    best_score = -100
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 2
        score = minimax(board, False)
        board[i][j] = 0
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def get_player_move(board):
    while True:
            move = int(input("Your move (1-9): "))
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != 0:
                print("Cell already taken, try again.")
                continue
            return row, col

def play_game():
    board = [[0] * 3 for _ in range(3)]

    clear_screen()
    print_score()
    print_positions()
    print_board(board)

    current_player = 1  # 1 = Player (X), 2 = Computer (O)

    while True:
        if current_player == 1:
            row, col = get_player_move(board)
            board[row][col] = 1
        else:
            print("Computer thinking")
            time.sleep(0.8)
            row, col = computer_move(board)
            board[row][col] = 2

        clear_screen()
        print_score()
        print_positions()
        print_board(board)

        if check_winner(board, current_player):
            if current_player == 1:
                score["Wins"] += 1
                print("Player wins")
            else:
                score["Losses"] += 1
                print("Computer wins")
            time.sleep(1.5)
            break

        if is_board_full(board):
            score["Draws"] += 1
            print("draw")
            time.sleep(1.5)
            break

        current_player = 2 if current_player == 1 else 1

def main():
    while True:
        play_game()

if __name__ == "__main__":
    main()