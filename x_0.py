#Крестики-нолики
board = [['-'] * 3 for _ in range(3)]
count = 0
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
                if count % 2:
                    board[gamer[0]][gamer[1]] = "0"
                else:
                    board[gamer[0]][gamer[1]] = "X"
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
            combo = [[board[i][0],board[i][1], board[i][2]], [board[0][i], board[1][i], \
                    board[2][i]], [board[0][0], board[1][1], board[2][2]], \
                     [board[2][0], board[1][1], board[0][2]]]
            for _ in combo:
                if len([i for i, n in enumerate(_) if n == x_o ]) == 3:
                    return True
def nex_game():
    #продолжение
    if input("Хотите сыграть еще? Введите Y или N ") == "Y":
        board = [['-'] * 3 for _ in range(3)]
        count = 0
        user()
    
while True:
    if count == 9:
        print("Ничья!")
        paint_board()
        nex_game()
    user(count)
    if count == 9:
        print()
    if win(count):
        if count % 2:
            x_o = "0"
        else:
            x_o = "X"
        paint_board()
        print(f"Победа игрока {x_o} !")
        nex_game()
        break
    count += 1
    continue
 