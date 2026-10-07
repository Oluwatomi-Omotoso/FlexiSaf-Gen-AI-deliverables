import random


def show_board(board):
    print("\n")
    for row in range(3):
        print(f" {board[row][0]} | {board[row][1]} | {board[row][2]} ")
        if row < 2:
            print("---+---+---")
    print("\n")


def check_winner(board, mark):
    # Check rows & columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def computer_move(board):
    # Find all open slots
    open_spots = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                open_spots.append((r, c))

    if open_spots:
        return random.choice(open_spots)
    return None


def main_game_loop():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    print("Tic-Tac-Toe vs Computer")
    print("Enter row and col from 1 to 3 separated by space (e.g. '2 2')")

    playing = True
    while playing:
        show_board(board)

        # Player's turn
        valid_input = False
        while not valid_input:
            move = input("Your move (row col): ").split()
            if len(move) != 2:
                print("Please enter two numbers.")
                continue

            try:
                r = int(move[0]) - 1
                c = int(move[1]) - 1
                if 0 <= r <= 2 and 0 <= c <= 2:
                    if board[r][c] == " ":
                        board[r][c] = "X"
                        valid_input = True
                    else:
                        print("That spot is taken!")
                else:
                    print("Numbers must be between 1 and 3.")
            except ValueError:
                print("Numbers only, please.")

        if check_winner(board, "X"):
            show_board(board)
            print("You won!")
            break

        if check_tie(board):
            show_board(board)
            print("Game's a tie.")
            break

        # Computer's turn
        comp_spot = computer_move(board)
        if comp_spot:
            board[comp_spot[0]][comp_spot[1]] = "O"
            print(f"Bot picked position: {comp_spot[0] + 1}, {comp_spot[1] + 1}")

        if check_winner(board, "O"):
            show_board(board)
            print("Bot wins.")
            break

        if check_tie(board):
            show_board(board)
            print("Game's a tie.")
            break


if __name__ == "__main__":
    main_game_loop()
