import random

num_digits = 3
max_guess = 10

#возвращает строку уникальных случайных цифр, длиной 3
def getSecretNum():
    num = list(range(10))
    random.shuffle(num)
    secret = ''
    for i in range(num_digits):
        secret += str(num[i])
    return secret

#возвращает строку с подсказками тепло,горячо, холодно
def getClues(guess, secret):
    if guess == secret:
        return 'Вы угадали!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append('Горячо!')
        elif guess[i] in secret:
            clues.append('Тепло')
    if len(clues) == 0:
        return 'Холодно'
    clues.sort()
    return ' '.join(clues)

#Возвращает true, eсли num - строка, состоящая только из цифр
def isOnlyDigits(num):
    return num.isdigit()

def introduction():
    print('Я загадаю %s - x значное число, которое вы долдны отгадать.' %(num_digits))
    print('Я дам несколько подсказок...')
    print('Когда я говорю:      Это означает')
    print(' Холодно              Ни одна цифра не отгадана.')
    print(' Тепло                Одна цифра отгадана, но не отгадана ее позиция.')
    print(' Горячо               Одна цифра и ее позиция отгаданы.')
    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.' % max_guess)

while True:
    secret = getSecretNum()
    introduction()
    attempts = 1
    while attempts <= max_guess:
        print('Попытка №%s: ' %(attempts))
        guess = input()

        print(getClues(guess, secret))
        attempts += 1

        if guess == secret:
            break
    print('Попыток больше не осталось. Я загадал число %s' %(secret))

    print('Хотите сыграть еще раз? (да ил нет)')
    if input() == 'нет':
        break


