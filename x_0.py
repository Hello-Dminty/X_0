#Крестики-нолики
board = [['-'] * 3 for _ in range(3)]
count = 0
all_games = []
#board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
def paint_board():
    #рисует игровое поле
    print ("  0 1 2" )
    for _ in range(3):
        print(f"{_} {' '.join(board[_])}")

def user(count=0):
    #Игрок ставит свою метку на поле
    while True:
        paint_board()
        gamer = input("Ввести цифру вертикально и горизонтально через пробел ").split()
        if gamer[0].isdigit() and gamer[1].isdigit():
            gamer = list(map(int, gamer))
            if 0 <= gamer[0] <= 2 and 0 <= gamer[1] <= 2 and board[gamer[0]][gamer[1]] == "-" \
            and len(gamer) == 2:
                L,R = gamer
                if count % 2:
                    board[L][R] = "0"
                else:
                    board[L][R] = "X"
                count += 1
                return count
            print("Неверный ввод. Ввести цифру вертик. и горизонт. через пробел ")    
            continue
        else:
            print("Неверный ввод. Ввести цифру вертик. и горизонт. через пробел ") 
            continue

def win(begin):
    #Проверка победы
    if begin % 2:
        x_o = "0"
    else:
        x_o = "X"
    for i in range(3):
        for i in range(3):
            combo = [[board[i][0], board[i][1], board[i][2]], [board[0][i], board[1][i], \
                    board[2][i]], [board[0][0], board[1][1], board[2][2]], \
                     [board[2][0], board[1][1], board[0][2]]]
            for _ in combo:
                if len([i for i, n in enumerate(_) if n == x_o ]) == 3:
                    return True

while True:
    #цикл игры
    if count == 9:
        print("Ничья!")
        paint_board()
        if input("Хотите сыграть еще? Введите Y ") == "Y":
            board = [['-'] * 3 for _ in range(3)]
            count = 0
            continue
        else:
            break
    user(count)
    if win(count):
        if count % 2:
            winer = "0"
        else:
            winer = "X"
        all_games += winer
        paint_board()
        print(f"Победа игрока {winer}. Победы Х: {all_games.count('X')}, "
        f"Победы 0: {all_games.count('0')}!")
        if input("Хотите сыграть еще? Введите Y ") == "Y":
            board = [['-'] * 3 for _ in range(3)]
            count = 0
            continue
        else:
            break
    count += 1
    continue
 