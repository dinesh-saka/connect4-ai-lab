# Random AI, Minimax AI, AlphaBetaAI
import random

class RandomAI:
    def get_move(self, board):
        valid_moves = board.get_valid_moves()
        return random.choice(valid_moves)

class RuleBasedAI():
    # If i can win now -> win
    # Else if human can win next turn -> block
    # Else random move

    def __init__(self, player):
        self.player=player

    def get_move(self, board):
        opponent = 1 if self.player == 2 else 2

        valid_moves = board.get_valid_moves()
        for move in valid_moves:
            temp_board = board.clone()
            temp_board.drop_piece(move, self.player)
            if temp_board.check_win(self.player):
                return move
        
        for move in valid_moves:
            temp_board = board.clone()
            temp_board.drop_piece(move, opponent)
            if temp_board.check_win(opponent):
                return move
            
        return random.choice(valid_moves)
