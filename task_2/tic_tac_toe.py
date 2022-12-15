BOARD = list(range(1,10))
WINS_COORDS = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw_board():
    print('-------------')
    for i in range(3):
        print('|', BOARD[0+i*3], '|', BOARD[1+i*3], '|', BOARD[2+i*3], '|')
    print('-------------')

def take_input(player_token):
    while True:
        value = input('Куда поставить: ' + player_token + ' ?')
        if not (value in '123456789'):
            print('Ошибочный ввод, повторите')
            continue
        value = int(value)
        if str(BOARD[value - 1]) in 'XO':
            print('Эта клетка занята')
            continue
        BOARD[value - 1] = player_token
        break

def chek_win():
    for each in WINS_COORDS:
        if (BOARD[each[0] - 1] == BOARD[each[1] - 1] == BOARD[each[2] - 1]):
            return BOARD[each[1] - 1]
        else:
            return False

def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = chek_win()
            if winner:
                draw_board()
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья!')
            break

main()