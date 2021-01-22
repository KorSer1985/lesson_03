### Примеры встроенных функций (range, ord, sorted) ###
words = ["banana", "Apple", "berry", "strawberry", "Blueberry", "apricot"]
words_sorted_wrong = sorted(words)
words_sorted = sorted(words, key=str.lower)
chars = ['a', 'A', 'c']
chars_ord = list(map(ord, chars))
# new_chars = [] #how maps work
# for el in chars:
#     new_el = ord(el)
#     print(el, new_el)
#     new_chars.append(new_el)
# print(chars)
# print(chars_ord)
# print(chr(0))
# # print(new_chars)
# print(words)
# print(words_sorted)
### именные функции
"""
def func_name(arg1, arg2):
    do something
"""
# alice = "Alice"
# b = 'Bob'
# def print_names(name1, name2="Bob"):
#     print(f'Hello, {name1}! Hello, {name2}!')
#     # return None
# print_names()


#### Оператор return #####
'''
def func_name(arg1, arg2):
    do something
    return something
'''

### Аргументы: позиционные, именнованные, обязательные, необязательные
def print_None(b, a=None):
    """
    Print something
    :param b:
    :param a:
    :return:
    """
    print(a)
    return b


# print_None()
"""
def user_info(name, mobile, email = None, phone = None):
    print(f'User info: {name}, {mobile}, {email}, {phone}')
user_info("Basil", "000")
"""

### *args and **kwargs

# def print_many_names(**kwargs):
#     for name in kwargs.keys():
#         print(f'Hello, {name, kwargs[name]}!')
#     # return None
#
# print_many_names(g1 = 'Bill', g2 = 'Basil', g3 = 'Bob')

### Видимость переменных: локальная, глобальная, нелокальная
"""
z = 10
def random_func(x, y):
    global z
    z = x + y
    return chr(z)
print(random_func(25,36))
print(z)
"""

### Анонимные функции (лямбда функции) и функция sorted
"""
lambda x: x**2
lambda x, y: x**2 + y**2

"""
features = [{'название': 'computer', 'цена': '500', 'количество': '3'},
            {'название': 'tv', 'цена': '200', 'количество': '5'},
            {'название': 'printer', 'цена': '350', 'количество': '1'}]

features_sorted_price = sorted(features, key = lambda x: int(x['цена'])*80)
# print(features_sorted_price)
x = list(map(lambda x: int(x['цена']) * 80, features))
print(x)
"""
1. Сделать через лямбда функции обновление словаря со стоимостью
2. Задача на рейтинг с именами
3. Задачу на заглавные из домашней работы сделать ord()
"""

# test_xy_lambda = lambda x, y: x**2 + y**2
# print(test_xy_lambda(3,2))

for i in range(0,10,2):
    print(i)
