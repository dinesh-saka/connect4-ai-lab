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
    def is_draw(self):
        if not self.get_valid_moves():
            return True
        return False
    def clone(self):
        return copy.deepcopy(self)