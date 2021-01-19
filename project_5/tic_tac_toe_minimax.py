# Global variables

# Initialize the grid as [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# This way, for example, index 1 corresponds to element 1
main_grid = list(range(1, 10))
main_grid.insert(0, None)
human_turn = True


def show_grid():
    """
    Print the 3x3 tic-tac-toe grid
    :return: None
    """
    for i in range(1, 8, 3):
        print(f"{main_grid[i]} | {main_grid[i + 1]} | {main_grid[i + 2]}")
        if i != 7:
            print("_"*9)


def choose_a_pos():
    """
    Function that allows the human player to select a position on the grid
    :return: None
    """
    while True:
        try:
            choice = int(input("Choose a position on the grid: [1-9]"))
            if 0 < choice < 10:
                if isinstance(main_grid[choice], str):
                    print("[ERROR] This position is already taken.", end=" ")
                else:
                    main_grid[choice] = human_player
                    show_grid()
                    break
            else:
                print("[ERROR] Enter an integer number between 1 and 9.", end=" ")
        except ValueError:
            print("[ERROR] Enter an integer number.", end=" ")


def winner(grid):
    """
    Function to evaluate the state of the game
    :return: 0 - continue the game; 1 - human player is the winner; 2 - computer player is the winner; 3 - it's a tie
    """
    x_winner = "XXX"
    o_winner = "OOO"

    # Horizontal lines
    line = str()
    for i in range(1, 8, 3):
        for j in range(3):
            line += str(grid[i + j])
        if (line == x_winner and human_player == 'X') or (line == o_winner and human_player == 'O'):
            return 1
        elif (line == x_winner and computer_player == 'X') or (line == o_winner and computer_player == 'O'):
            return 2
        line = str()

    # Vertical lines
    for i in range(1, 4):
        for j in range(0, 7, 3):
            line += str(grid[i + j])
        if (line == x_winner and human_player == 'X') or (line == o_winner and human_player == 'O'):
            return 1
        elif (line == x_winner and computer_player == 'X') or (line == o_winner and computer_player == 'O'):
            return 2
        line = str()

    # Diagonal lines
    lines = [str(grid[1]) + str(grid[5]) + str(grid[9]), str(grid[3]) + str(grid[5]) + str(grid[7])]
    for line in lines:
        if (line == x_winner and human_player == 'X') or (line == o_winner and human_player == 'O'):
            return 1
        elif (line == x_winner and computer_player == 'X') or (line == o_winner and computer_player == 'O'):
            return 2

    # Tie
    numbers = "123456789"
    for i in range(10):
        if str(grid[i]) in numbers:
            return 0
    return 3


def minimax(maximizing, depth, grid):
    """
    The minimax algorithm
    :param maximizing: Boolean variable which is true when it's the computer turn and false otherwise
    :param depth: The number of recursive calls
    :param grid: The current grid according to the state of the algorithm
    :return: The value of each move
    """
    if winner(grid) == 1:               # The human would win
        return -10
    elif winner(grid) == 2:             # The computer would win
        return 10
    elif winner(grid) == 3:             # It would be a tie
        return 0

    # If winner(grid) == 0 (that is, the game needs to continue)
    if maximizing:
        # There will certainly be a bigger number than -1000
        best = -1000
        for elem in grid:
            if isinstance(elem, int):
                grid[elem] = computer_player
                best = max(best, minimax(not maximizing, depth+1, grid))
                grid[elem] = elem
        return best
    else:
        # There will certainly be a smaller number than 1000
        best = 1000
        for elem in grid:
            if isinstance(elem, int):
                grid[elem] = human_player
                best = min(best, minimax(not maximizing, depth + 1, grid))
                grid[elem] = elem
        return best


def set_pos():
    """
    Function that allows the computer player to select a position on the grid
    :return: None
    """
    best_move = None                                # None will be replaced by the index of the computer move
    best_move_val = -1000
    for elem in main_grid:
        if isinstance(elem, int):
            aux_grid = list(main_grid)
            aux_grid[elem] = computer_player
            move_val = minimax(False, 0, aux_grid)
            if move_val > best_move_val:
                best_move = elem
                best_move_val = move_val
    main_grid[best_move] = computer_player
    show_grid()


# Choose a playing symbol
human_player = input("Player 1: Choose a symbol [X/O]: ").upper().strip()
while human_player not in "XO":
    human_player = input("Invalid input. Enter 'X' or 'O': ")
if human_player == "X":
    computer_player = "O"
else:
    computer_player = "X"
print(f"Human player: {human_player}\nComputer player: {computer_player}")


# Game loop
show_grid()
while True:
    if human_turn:
        print("It's your turn now.")
        choose_a_pos()
    else:
        print("It's the computer turn now.")
        set_pos()
    if winner(main_grid) == 1:
        print("Machine won't defeat us! Congratulations, human!")
        break
    elif winner(main_grid) == 2:
        print("The computer won. It can only be attributable to human error.")
        break
    elif winner(main_grid) == 3:
        print("It's a tie")
        break
    # Swap turns
    human_turn = not human_turn
