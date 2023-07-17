def print_board(board):
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(" " + cell + " ", end="|")
        print("\n-------------")

def check_win(board, player):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == player) or \
           (board[0][i] == board[1][i] == board[2][i] == player) or \
           (board[0][0] == board[1][1] == board[2][2] == player) or \
           (board[0][2] == board[1][1] == board[2][0] == player):
            return True
    return False

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    game_over = False

    while not game_over:
        print_board(board)

        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = players[current_player]

        if check_win(board, players[current_player]):
            print_board(board)
            print("Player", players[current_player], "wins!")
            game_over = True
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            game_over = True

        current_player = (current_player + 1) % 2

play_tic_tac_toe()
