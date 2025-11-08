def main():
    while True:
        print("=" * 30)
        print(" " * 8 + 'Редактор строк')
        print("=" * 30)
        stroka = input('Вставьте вашу строку: ')

        if not stroka.strip():
            print("Ошибка: Строка не может быть пустой!\n")
            continue

        while True:
            for index, text in enumerate(vibor.keys(), 1):
                print(f"{index}) {text}")

            try:
                user_vibor = int(input("Выберите доступный вариант: "))

                if user_vibor < 1 or user_vibor > len(vibor):
                    print(f"Ошибка: Введите число от 1 до {len(vibor)}!\n")
                    continue


                if user_vibor == len(vibor):
                    print("До свидания!")
                    return

                var = list(vibor.values())[user_vibor - 1]
                var(stroka)
                break

            except ValueError:
                print("Ошибка: Введите корректное число!\n")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}\n")


def shifr(stroka):
    print('Добро пожаловать в шифратор')
    while True:
        try:
            smehenye = int(input('На сколько элементов сдвинуть исходную букву: '))
            break
        except ValueError:
            print("Ошибка: Введите целое число!")

    result = []
    for stok in stroka:
        result.append(ord(stok) + smehenye)

    print(f"Ваш зашифрованный текст со смещением на {smehenye} элементов:")
    print(*[chr(i) for i in result], sep='')
    print()


def deshifr(stroka):
    print('Добро пожаловать в дешифратор')
    while True:
        try:
            smehenye = int(input('На сколько элементов вы сдвигали исходную букву: '))
            break
        except ValueError:
            print("Ошибка: Введите целое число!")

    result = []
    for stok in stroka:
        result.append(ord(stok) - smehenye)

    print(f"Ваш исходный текст со смещением на {smehenye} элементов:")
    print(*[chr(i) for i in result], sep='')
    print()


def analyz_texta(stroka):
    print("Добро пожаловать в аналитику строки")
    print(f'Длина вашей строки = {len(stroka)}')
    print(f"Количество пробелов: {stroka.count(" ")}")
    print(f"Количество слов: {len(stroka.split())}")
    print()


def format_texta(stroka):
    print("Добро пожаловать в форматирование строки")
    print(f"В верхнем регистре: {stroka.upper()}")
    print(f"В нижнем регистре: {stroka.lower()}")
    print(f"С заглавных букв: {stroka.title()}")
    print()


vibor = {"Шифрование": shifr,
         "Дешифрование": deshifr,
         "Анализ текста": analyz_texta,
         "Форматирование текста": format_texta,
         "Выход": None}

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем. До свидания!")
    except Exception as e:
        print(f"\nКритическая ошибка: {e}")