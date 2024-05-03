class Board:
    """Класс для отображения игрового поля."""
    FIELD_SIZE = 3

    def __init__(self):
        self.field_size = self.FIELD_SIZE
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        for i in range(self.field_size):           
            if all([self.board[i][j] == player for j in range(self.field_size)]):
                return True
        for j in range(self.field_size):           
            if all([self.board[i][j] == player for i in range(self.field_size)]):
                return True 
        if all([self.board[k][k] == player for k in range(self.field_size)]):
            return True           
        if all([self.board[k][self.field_size - k - 1] == player for k in range(self.field_size)]):
            return True 
        return False
