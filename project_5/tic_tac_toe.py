def show_grid():
    """
    Print the 3x3 tic-tac-toe grid
    :return: None
    """
    for i in range(1, 8, 3):
        print(f"{grid[i]} | {grid[i+1]} | {grid[i+2]}")
        if i != 7:
            print("_"*9)


def choose_a_pos(player):
    """
    Function that allows the current player to select a position on the grid
    :param player: Receive one of the two players as parameters
    :return: None
    """
    while True:
        try:
            choice = int(input("Choose a position on the grid: [1-9]"))
            if 0 < choice < 10:
                if isinstance(grid[choice], str):
                    print("[ERROR] This position is already taken.", end=" ")
                else:
                    grid[choice] = player
                    show_grid()
                    break
            else:
                print("[ERROR] Enter an integer number between 1 and 9.", end=" ")
        except ValueError:
            print("[ERROR] Enter an integer number.", end=" ")


def winner():
    """
    Function to evaluate the state of the game
    :return: 0 - continue the game; 1 - one winner; 2 - it's a tie
    """
    x_winner = "XXX"
    o_winner = "OOO"

    # Horizontal lines
    line = str()
    for i in range(1, 8, 3):
        for j in range(3):
            line += str(grid[i+j])
        if line == x_winner or line == o_winner:
            return 1
        line = str()

    # Vertical lines
    for i in range(1, 4):
        for j in range(0, 7, 3):
            line += str(grid[i+j])
        if line == x_winner or line == o_winner:
            return 1
        line = str()

    # Diagonal lines
    lines = [str(grid[1]) + str(grid[5]) + str(grid[9]), str(grid[3]) + str(grid[5]) + str(grid[7])]
    for line in lines:
        if line == x_winner or line == o_winner:
            return 1

    # Tie
    numbers = "123456789"
    for i in range(10):
        if str(grid[i]) in numbers:
            return 0
    return 2


# Chose a playing symbol
player_1 = input("Player 1: Choose a symbol [X/O]: ").upper().strip()
while player_1 not in "XO":
    player_1 = input("Invalid input. Enter 'X' or 'O': ")
if player_1 == "X":
    player_2 = "O"
else:
    player_2 = "X"
print(f"Player 1: {player_1}\nPlayer 2: {player_2}")

# Initialize the grid as [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# This way, for example, index 1 corresponds to element 1

grid = list(range(1, 10))
grid.insert(0, None)
show_grid()
player_1_turn = True

# Game loop

while True:
    if player_1_turn:
        print("It's player 1 turn now.")
        choose_a_pos(player_1)
    else:
        print("It's player 2 turn now.")
        choose_a_pos(player_2)
    if winner() == 1:                           # If there is one winner, it's the last player who made a move
        if player_1_turn:
            print("The winner is player 1")
        else:
            print("The winner is player 2")
        break
    elif winner() == 2:
        print("It's a tie")
        break
    # Swap turns
    player_1_turn = not player_1_turn
