def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params()  #Попробовал разные комбинации ему норм
print_params(3, 'test', False)  #Возможно если бы были ещё команды внутри функции
print_params(1, False)  #то он бы ругался
print_params('123', 123, '321')
print_params('asd', 4.3, 'qwe')
print_params(b=25)
print_params(c=[1, 2, 3])
print()

value_list = [False, 'Qwerty', 321]                         #Все работает как в лекции
value_dict = {'a': 321, 'c': False, 'b': 'строка'}
print_params(*value_list)
print_params(**value_dict)
print()

value_list_2 = ['qwe', 4.5]                                  #Тут тоже всё работает
print_params(*value_list_2, 42)
