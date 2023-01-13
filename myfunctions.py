"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""

# 1. Функция создает красивый резделитель из 10-и звездочек (**********)

def simple_separator():
    return '*'*10

print(simple_separator() == '**********')  # True


# 2. Функция создает разделитель из звездочек число которых можно регулировать параметром count

def long_separator(count):
    return '*'*count

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True




# 3. Функция создает разделитель из любых символов любого количества

def separator(simbol, count):
    return simbol*count


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


# 4. Функция печатает Hello World в формате:

def hello_world():
    print(simple_separator())
    print('Hello World!')
    print(separator('#', 10))
    return None
 
hello_world()  # вызываем функцию hello_world



# 5. Функция печатает приветствие в красивом формате

def hello_who(who='World'):

    print(simple_separator())
    print('Hello {}!'.format(who))
    print(separator('#', 10))
    return None

hello_who()





# 6. Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)

def pow_many(power, *args):
    sum = 0
    for i in args:
        sum += i
    return sum**power


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


# 7. Функция выводит переданные параметры в фиде key --> value

def print_key_val(**kwargs): # передаем любое количество параметров по имени: имя -> значение в любой последовательности
    for k, v in kwargs.items():  # проходим в цикле
        print(f'{k} --> {v}')    # форматированный вывод

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)





# 8. Функция фильтрует последовательность iterable и возвращает новую
# Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет

def my_filter(iterable, function):
    new_list = []
    for i in iterable:
        if function(i):
            new_list.append(i)
    return new_list


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
