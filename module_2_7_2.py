def get_multiplied_digits(number=50):
    str_number = str(number)
    str_number = str_number.replace('0', '')
    try:                                # при нуле и строке оно ругается, решил исключить
        first = int(str_number[0])
    except IndexError:
        return 'Кажется вы ввели нуль'
    except ValueError:
        return 'Что-то мне подсказывает ввели вы ненатуральное число('
    if len(str_number) == 1 and number != 0:
        return int(str_number)
    try:
        return first * get_multiplied_digits(int(str_number[1:]))
    except ValueError:
        return 'Что-то мне подсказывает ввели вы ненатуральное число('


print(get_multiplied_digits(5034))
print(get_multiplied_digits(0))
print(get_multiplied_digits('123'))
print(get_multiplied_digits('f'))
print(get_multiplied_digits('1g'))
