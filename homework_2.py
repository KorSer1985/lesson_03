#### Домашняя работа
# задача 2
my_list = list(input('Введите текст: '))
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)


# задача 4
line = input('Введите текст: ')
words = line.split()
for i, word in enumerate(words):
    print(i, word[:10])

# задача 5
my_list = [7, 5, 3, 3, 2]
request = input('Введите число: ')
for index, number in enumerate(my_list):
    if int(request) < int(number):
        continue
    my_list.insert(index, request)
    break
else:
    my_list.append(request)
print(my_list)

# задача 5.1
my_list = [7, 5, 3, 2, 1]
element = input('Введите новый элемент списка: ')
if element.isdigit() and int(element) >= 0:
    my_list.append(int(element))
    my_list.sort(reverse=True)
    print('Список ', my_list)

# задача 6

goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        if (f == 'цена' or f == 'количество'):
            features[f] = int(user_data)
        else:
            features[f] = user_data
        # features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features.copy()))
    print('Текущая аналитика по товарам:\n')
    print(analitics)
    # for key, value in analitics.items():
    #     print(key, value)
