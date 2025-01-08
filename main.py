def print_params(a=1, b='строка', c=True):
    print(a,b,c)
#-функции с разным количеством аргументов:
print_params(3,'arg')
print_params(9,None,False)
print_params(18)
print_params()
#
print_params(b=25)
print('f print_params(b=25)hf,работает')
print_params(c=[1, 2, 3])
print('f print_params(c=[1, 2, 3])работает')

values_list=[456,None,'str'] #-создать список с тремя элементами разных типов.
print_params(*values_list)
#- создать словарь с тремя ключами,соответствующими параметрам  функции print_params,и разных типов.
values_dict={'a':987,'b':'слово','c':False}
print_params(**values_dict)

# - создадим список  values_list_2 с двумя элементами разных типов.
values_list_2 = ['Год', 2025 ]

 #проверим,работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print('fprint_params(*values_list_2, 42)работает')

