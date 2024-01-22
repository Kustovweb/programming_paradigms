import os
name_os = os.name
def clear_console():
    if name_os == 'nt':
        _ = os.system("cls")
    else:
        _ = os.system("clear")

white_blue = "\033[1;97;44m"
white_red = "\033[1;97;41m"
white_green = "\033[1;97;42m"
reset_color = "\033[0m"
    
board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    '''Вывод игрового поля'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * board_size], '|', board[1 + i * board_size], '|', board[2 + i * board_size], '|')
        print(('_' * 3 + '|') * 3)



def game_step(index, char):
    '''Выполняем ход'''
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False
    board[index - 1] = char
    return True

def check_winner():
    '''Проверка выигрыша'''
    win = False

    win_rules = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    )

    for pos in win_rules:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]

    return win

def start_game():
    '''Старт игры'''
    current_player = f'{white_green}X{reset_color}'
    step = 1
    draw_board()
    
    while step < 10 and check_winner() == False:
        index = input(f'Ходит игрок {current_player}. Введите номер поля, Для выхода введите 0: ')
        if index == '0':
            break
        if game_step(int(index), current_player):
            print('Удачный ход')
            clear_console()
            draw_board()
            step += 1

            if current_player == f'{white_green}X{reset_color}':
                current_player = f'{white_blue}O{reset_color}'
            else:
                current_player = f'{white_green}X{reset_color}'
        else:
            print('Неверный номер, повторите ход')
    if step == 9:
        print("Ничья!")
    else:
        print(f'Выиграл {check_winner()}')
        


start_game()


# Использовал структурную парадигму и фунциональную, хотя лучше подходит ОО парадигма