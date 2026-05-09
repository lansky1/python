player_dict = {"Player 1": "", "Player 2": ""}
board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
occupied_positions = []
current_turn = ""
game_on = True


# Functions
def accept_valid_symbol():
    symbol = ""
    while symbol not in ["X", "O", "Q"]:
        symbol = input(
            "\nPlayer 1, please choose your symbol (X/O) (Press q to Quit): "
        ).upper()

        if symbol not in ["X", "O", "Q"]:
            print("Please choose valid symbol.")

    return symbol


def accept_valid_position(symbol):
    while True:
        user_input = input(
            "\n{}, please select the position where you want to put {} (Press 0 to Quit): ".format(
                symbol, player_dict[symbol]
            )
        )

        if not user_input.isdigit():
            print("Please choose valid position.")
            continue

        pos = int(user_input)

        if pos not in range(0, 10):
            print("Please choose valid position.")
        elif pos in occupied_positions:
            print("This position is occupied. Please choose another position.")
        else:
            return pos


def print_board():
    for row_index, row in enumerate(board):
        print(" | ".join(row))

        if row_index < len(board) - 1:
            print("----------")


# Start Game
print("Welcome to Tic Tac Toe!\n")

print_board()

player_dict["Player 1"] = accept_valid_symbol()
player_dict["Player 2"] = "X" if player_dict["Player 1"] == "O" else "O"
current_turn = player_dict["Player 1"]

if player_dict["Player 1"] == "Q":
    game_on = False

current_turn = "Player 1"

while game_on:
    pos = accept_valid_position(current_turn)
    if pos == 0:
        game_on = False
        continue

    occupied_positions.append(pos)

    board[(pos - 1) // 3][(pos - 1) % 3] = player_dict[current_turn]

    print_board()

    current_turn = "Player 2" if current_turn == "Player 1" else "Player 1"

    # How can a game end?
    # All slots are filled
    if len(occupied_positions) == 9:
        print("Game drawn!\n")
        game_on = False
    # Someone wins
