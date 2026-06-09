# chose mode, start game
from board import Board
from ai import RandomAI, RuleBasedAI

board = Board()
ai = None
random_ai = RandomAI()
rule_ai = RuleBasedAI(2)
curr_player = 1


game_mode = int(input(
    "Choose game mode:- \n"
    "[1] Human vs Human\n"
    "[2] Human vs Random AI (lvl 1)\n"
    "[3] Human vs Rule Based AI (lvl 2)\n"
))

if game_mode == 2:
    ai = random_ai
elif game_mode == 3:
    ai = rule_ai

def human_input():
    while True:
        col = int(input("Column: ")) - 1

        if col < 0 or col >= board.cols:
            print("Enter valid column")
            continue

        elif not board.is_valid_column(col):
            print("Invalid move")
            continue
        
        return col

while True:
    if board.is_draw():
        print("Draw!")
        break

    board.print_board()
    print(f"Player {curr_player} turn")

    if game_mode == 1:
        # human vs human
        col = human_input()
    else:
        # human vs AI
        if curr_player == 1:
            col = human_input()
        else:
            col = ai.get_move(board)
            print(f"AI chose column {col+1}")
    
    board.drop_piece(col, curr_player)
        
    if board.check_win(curr_player):
        print(f"Player {curr_player} wins!")
        board.print_board()
        break
    
    if curr_player == 1:
        curr_player = 2
    else:
        curr_player = 1