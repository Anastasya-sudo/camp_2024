import random

def hangmon():
    print("Привет! Добро подаловать в игру Виселица")
    wordlist = ['мандарин', 'яблоко', 'груша', 'виноград', 'апельсин', 'манго']
    secret = random.choice(wordlist)
    guesses = 'ауоыиэяюёе'
    turns = 6

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1
        if missed == 0:
            print('\nТы выйграл!')
            break

        guess = input('\nНазови букву: ')
        guesses += guess

        if guess not in secret:
            turns -= 1
            print('\nНе угадал.')
            print('\n', 'Осталось попыток: ', turns)
            if turns < 6: print('\n   _____ ')
            if turns < 5: print('   |0 0| ')
            if turns < 4: print('   |___| ')
            if turns < 3: print('    | | ')
            if turns < 2: print('    |_| ')
            if turns < 1: print('   |_|_| ')
            if turns == 0: print('\n\nэто слово: ', secret)
ans = 'да'
while ans == 'да':
    hangmon()
    print('Хочешь сыграть еще раз? (да или нет)')
    ans = input()
