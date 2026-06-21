import copy

# Responsible for board state, checking wins, checking draws, printing board

class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
    def print_board(self):
        for row in self.grid:
            print("|", end=" ")
            for col in row:
                print(col, end=" | ")
            print("")
    
    def drop_piece(self, chosen_col, player):
        if not self.is_valid_column(chosen_col):
                return False
        for row in range(self.rows-1, -1, -1):
            if self.grid[row][chosen_col] == 0:
                self.grid[row][chosen_col] = player
                return True
            else:
                continue
    def is_valid_column(self, col):
        return self.grid[0][col] == 0
    
    def get_valid_moves(self):
        valid_moves = []
        for col in range(self.cols):
            if self.is_valid_column(col):
                valid_moves.append(col)
        return valid_moves
    
    def check_horz_win(self, player):
        for row in range(self.rows):
            for col in range(0, 4):
                if (
                    self.grid[row][col] == player and
                    self.grid[row][col+1] == player and
                    self.grid[row][col+2] == player and
                    self.grid[row][col+3] == player
                ):
                    return True
        return False
    def check_vert_win(self, player):
        for col in range(self.cols):
            for row in range(0, 3):
                if (
                    self.grid[row][col] == player and
                    self.grid[row+1][col] == player and
                    self.grid[row+2][col] == player and
                    self.grid[row+3][col] == player
                ):
                    return True
        return False
    def check_diag_win(self, player):
        for row in range(0, 3):
            for col in range(0, 4):
                if (
                    self.grid[row][col] == player and
                    self.grid[row+1][col+1] == player and
                    self.grid[row+2][col+2] == player and
                    self.grid[row+3][col+3] == player
                ):
                    return True
        for row in range(self.rows-1, self.rows-4, -1):
            for col in range(0, 4):
                if (
                    self.grid[row][col] == player and
                    self.grid[row-1][col+1] == player and
                    self.grid[row-2][col+2] == player and
                    self.grid[row-3][col+3] == player
                ):
                    return True 
        return False
    def check_win(self, player):
        if (self.check_diag_win(player) or 
            self.check_horz_win(player) or 
            self.check_vert_win(player)):
            return True
        return False
    
    def evaluate_window(self, window, piece):
        score = 0

        opp = 1 if piece == 2 else 2
        count_ai = window.count(piece)
        count_opp = window.count(opp)
        count_empty = window.count(0)

        if count_ai == 4:
            score += 100000
        if count_ai == 3 and count_empty == 1:
            score += 100
        if count_ai == 2 and count_empty == 2:
            score += 10
        
        if count_opp == 4:
            score -= 100000
        if count_opp == 3 and count_empty == 1:
            score -= 80
        if count_opp == 2 and count_empty == 2:
            score -= 5

        return score
    
    def score_position(self, piece):
        score = 0

        # center bonus
        center_col = self.cols // 2
        center_count = 0
        for row in range(self.rows):
            if self.grid[row][center_col] == piece:
                center_count += 1

        score += center_count * 3

        # horizontal evaluation
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [
                    self.grid[row][col],
                    self.grid[row][col+1],
                    self.grid[row][col+2],
                    self.grid[row][col+3]
                ]
                score += self.evaluate_window(window, piece)
        
        # vertical evaluation
        for row in range(self.rows - 3):
            for col in range(self.cols):
                window = [
                    self.grid[row][col],
                    self.grid[row+1][col],
                    self.grid[row+2][col],
                    self.grid[row+3][col]
                ]
                score += self.evaluate_window(window, piece)
        
        # positive diagonal evaluation (\)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [
                    self.grid[row][col],
                    self.grid[row + 1][col + 1],
                    self.grid[row + 2][col + 2],
                    self.grid[row + 3][col + 3]
                ]

                score += self.evaluate_window(window, piece)
        
        # negative diagonal evaluation (/)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [
                    self.grid[row][col],
                    self.grid[row - 1][col + 1],
                    self.grid[row - 2][col + 2],
                    self.grid[row - 3][col + 3]
                ]

                score += self.evaluate_window(window, piece)

        return score

    def is_draw(self):
        if not self.get_valid_moves():
            return True
        return False
    def clone(self):
        return copy.deepcopy(self)