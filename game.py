# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError

def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print('='*50, f'Ход делают {current_player}', sep='\n')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row not in range(game.field_size):
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))        
                if column not in range(game.field_size):
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError as e:
                print(e)
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break       

        
        # В метод make_move передаются те координаты, которые ввёл пользователь.
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            print(f'Победили {current_player}!')
            running = False
        if game.is_board_full():
            print('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()