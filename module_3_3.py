def print_params (a = 1, b = 'строка', c = True): #"Распаковка позиционных параметров"
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(b = 25, c = [1, 2, 3])
print_params()


values_list = [1,'two', 0.8] #список
values_dict = {'a':2, 'b':'вишня', 'c':False} #словарь


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)