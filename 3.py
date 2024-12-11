# Function to print Tic Tac Toe board
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Function to print the scoreboard
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t         SCOREBOARD      ")
    print("\t--------------------------------")
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
    print("\t--------------------------------\n")

# Function to check if any player has won
def check_win(player_pos, cur_player):
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            # Return True if any winning combination is satisfied
            return True
    # Return False if no combination is satisfied
    return False

# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

# Function for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe board
    values = [' ' for x in range(9)]
    
    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        # Try-except block for move input
        try:
            print("Player", cur_player, "turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input! Try Again.")
            continue

        # Sanity check for move input
        if move < 1 or move > 9:
            print("Wrong Input! Try Again.")
            continue

        # Check if the box is not occupied
        if values[move - 1] != ' ':
            print("Place already filled. Try again!")
            continue

        # Update game information
        values[move - 1] = cur_player
        player_pos[cur_player].append(move)

        # Check for win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player", cur_player, "has won the game!")
            print("\n")
            return cur_player

        # Check for draw
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player
        cur_player = 'O' if cur_player == 'X' else 'X'

if __name__ == "__main__":
    print("Player 1")
    player1 = input("Enter the name: ")
    print("\nPlayer 2")
    player2 = input("Enter the name: ")
    print("\n")

    # Stores the player who chooses X and O
    cur_player = player1
    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}
    # Stores the options
    options = ['X', 'O']
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}

    print_scoreboard(score_board)

    # Game loop for a series of Tic Tac Toe games
    while True:
        # Player choice menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # Try-except block for choice input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input! Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            player_choice['O'] = player2 if cur_player == player1 else player1
        elif choice == 2:
            player_choice['O'] = cur_player
            player_choice['X'] = player2 if cur_player == player1 else player1
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break
        else:
            print("Wrong Choice! Try Again\n")
            continue

        # Winner of a single game of Tic Tac Toe
        winner = single_game(options[choice - 1])

        # Update scoreboard based on the winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] += 1
        print_scoreboard(score_board)

        # Switch starting player for the next game
        cur_player = player2 if cur_player == player1 else player1
