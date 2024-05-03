# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    game.display()
    while True:
        try:
            # Тут пользователь вводит координаты ячейки.
            row = int(input('Введите номер строки: '))
            if row not in range(game.field_size):
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))        
            if column not in range(game.field_size):
                raise FieldIndexError
        except FieldIndexError as e:
            print(e)
            continue
        #except ValueError:
        #    print('Буквы вводить нельзя. Только числа.')
        #    print('Пожалуйста, введите значения для строки и столбца заново.')
        #    continue
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            continue
        else:
            break       

        
    # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()