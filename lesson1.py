str_1 = input('Введите строку без пробелов и с использованием только нижних регистров: ')
str_2 = str_1[::-1]
if str_1 == str_2:
    print (True)
else:
    print(False)