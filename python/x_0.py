# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "S" and maps[i[1]] == "S" and maps[i[2]] == "S":
            win = "S"
        if maps[i[0]] == "Z" and maps[i[1]] == "Z" and maps[i[2]] == "Z":
            win = "Z"
    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:
    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "S"
        step = int(input("Stev 1, ваш ход: "))
    else:
        symbol = "Z"
        step = int(input("Zombi 2, ваш ход: "))

    step_maps(step, symbol)  # делаем ход в указанную ячейку

    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)