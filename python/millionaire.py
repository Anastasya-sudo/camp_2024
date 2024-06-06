while True:
    print()
    print()
    print()
    print("Привет! Эта игра Кто хочет стать миллионером!")
    print("Как тебя зовут?")
    name = input("Ответ - ")
    print()
    print()
    print()
    print("Очень приятно, " + name)
    print("Итак, первый вопрос на 20рбк")
    print()
    print()
    print()

    bank = 0

    print("C какого месяца начинается зима?")
    print("А. Октябрь")
    print("Б. Ноябрь")
    print("В. Декабрь")
    print("Г. Январь")
    print()
    print()
    print()

    ans1 = input("Ответ - ")

    if ans1 == "В" or ans1 == "в":
        print("Это правильный ответ!")
        bank += 50
        print("Твой банк: " + str(bank))
    else:
        print("К сожалению, ответ неправильный(((")
        print("Игра окончена")
        print("Твой банк: " + str(bank))
        break
# вопросы генерят дети, после меняются местами и играют. bank = рбк за занятие