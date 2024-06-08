import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
который готов поделиться с вами своими сокровищами. 
Во второй —жадный и голодный дракон, который мигом вас съест.''')
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
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendly = random.randint(1, 2)

    if str(friendly) == cave:
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')

player = 'да'
while player == 'да' or player == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу снова? (да или нет)')
    player = input()


