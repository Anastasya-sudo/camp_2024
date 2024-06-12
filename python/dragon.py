import random
import time

def displayIntro():
    print('''Вы находитесь в «тёмных глубинах мира», где обитает новый вражденый моб - Варден.
Перед собой вы видите две пещеры. В одной из них — сундук с сокровищами. 
Во второй —Варден, он cчитается самым сильным боссом на момент выхода нового патча.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()
    return cave

def checkCave(cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Вы входите в нее и...')
    print()
    time.sleep(2)

    friendly = random.randint(1, 2)

    if str(friendly) == cave:
        print('...вы видите перед собой 5 сундуков с сокровищами!')
    else:
        print('Варден моментально атакует вас...!')

player = 'да'
while player == 'да' or player == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу снова? (да или нет)')
    player = input()



