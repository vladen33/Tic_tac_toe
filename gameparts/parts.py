class Board:
    """Класс для отображения игрового поля."""
    FIELD_SIZE = 3

    def __init__(self):
        self.field_size = self.FIELD_SIZE
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9) 
