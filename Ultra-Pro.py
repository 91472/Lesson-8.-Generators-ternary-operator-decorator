# Урок: Генераторы, тернарные операторы, исключения, декораторы
# Задание Ultra-Pro:
#1. Выполнить задание уровня pro
#2. В своем проекте переписать код с использованием генераторов и тернарных операторов;
#3. Где это возможно применить декораторы.


# Выполнение задания Ultra-Pro:
#1. Задание уровня pro выполнено: https://github.com/91472/Lesson-8.-Generators-ternary-operator-decorator/blob/7880f76c56c5c5ff85d6573088151cfad729841a/Pro.py

# Задание Ultra Pro:
#2. В своем проекте переписать код с использованием генераторов и тернарных операторов;
#3. Где это возможно применить декораторы.
# Позволю себе переформулировать это задание, т.к. в нем нет логики.
# Итак, необходимо переписать код предыдущих трех заданий (ultra-lite, lite и ultra-pro) с использованием генератора,
# тернарного оператора и декоратора там, где они не были применены ранее (т.к. в части заданий они уже были использованы)

# Переписываем код задания Ultra Lite с использованием генератора, тернарного оператора и декоратора (где это возможно):
# Формулировка задания из Ultra Lite: Написать свой генератор последовательностей, свой тернарный оператор, своей декоратор.
#БЫЛО:
gen_list_1 = [i for i in range(-10, 11) if i > 0] #список
print('Создание списка генератором последовательности (Задание ultra-lite):\n', gen_list_1, '\nтип объекта: ', type(gen_list_1), sep = '')
#СТАЛО:
def gen(): #применение функции-генератора в соответствии с требованием задания
    for i in gen_list_1:
           j = i if i > 0 else 0    #применение тернарного оператора в соответствии с требованием задания
           yield j
print('\nСоздание списка генератором (Задание ultra-pro): \n', list(gen()), '\nтип функции:', type(gen()), sep = '')

#БЫЛО:
print('\nВывод на экран через генератор последовательности (Задание ultra-lite):')
gen_list_2 = [print(i,'**',j, '=', i**j) for i,j in enumerate(gen_list_1) if i > 5] #вывод на экран генератором последовательности
#СТАЛО:
print('\nВывод на экран через функцию-генератор (Задание ultra-pro):')
def gen1(): #применение функции-генератора в соответствии с требованием задания
    for i, j in enumerate(gen_list_1):
        if i > 5:
            yield print(i,'**',j, '=', i**j if i**j > 10 else 0) #применение тернарного оператора в соответствии с требованием задания
list(gen1())
print('Тип функции: ', type(gen1()))

#БЫЛО:
gen_dict = {i: j for i,j in enumerate(gen_list_1)} #словарь
print('\nСоздание словаря генератором последовательности (Задание ultra-lite):\n', gen_dict, '\nТип объекта: ', type(gen_dict), sep = '')
#СТАЛО:
print('\nСоздание словаря функцией-генератором (Задание ultra-pro):')
def gen2(): #применение функции-генератора в соответствии с требованием задания
    for i, j in enumerate(gen_list_1):
        k = i if i > 0 else 0 #применение тернарного оператора в соответствии с требованием задания
        yield i,j
print(dict(gen2()), '\nТип функции: ', type(gen2()), sep = '')

#БЫЛО:
gen_set = {i for i,j in enumerate(gen_list_1)} #множество
print('\nСоздание множества генератором последовательности (Задание ultra-lite):\n', gen_set, '\nТип объекта: ', type(gen_set), sep = '')

#СТАЛО:
print('\nСоздание множества функцией-генератором (Задание ultra-pro):')
def gen3(): #применение функции-генератора в соответствии с требованием задания
    for k in enumerate(gen_list_1):
        i = k[0] if k[0] > -1 else None #применение тернарного оператора в соответствии с требованием задания
        yield i
print(set(gen3()), '\nТип функции: ', type(gen3()), sep='')

#БЫЛО:
#Создадим тернарный оператор внутри генератора последовательностей (если число четное, оставить, если нет, то заменить на символ *):
gen_ternary = [i if i%2 == 0 else '*' for i in range(1, 10)]
print('\nИспользование тернарного оператора совместно с генератором последовательности (Задание ultra-lite):\n', gen_ternary, sep = '')
#СТАЛО:
print('\nИспользование тернарного оператора совместно с функцией-генератором (Задание ultra-pro):')
def gen4(): #применение функции-генератора в соответствии с требованием задания
    for i in range(1,10):
        k = i if i%2 == 0 else '*' #применение тернарного оператора в соответствии с требованием задания
        yield k
print([i for i in gen4()], '\nТип функции: ', type(gen4()), sep='')

# Декоратор уже был написан в задании ultra-lite, поэтому напишем еще один и применим каскадно два декоратора.
# 2. Написать свой декоратор (задание из ultra-lite)
#Создадим декоратор выводящий до вызова функции на экран кортеж неименованных параметров и словарь именованных параметров функции,
#И после вызова функции выводится текущая дата и время

import datetime #импортируем бидлиотеку работ с датой и временем
def args_time(f): #создаем декоратор
    def wrapper(*args, **kwargs): #обертка функции которая подается на декоратор
        print('\nКортеж из неименованных параметров: ', args, '\nСловарь из именованных параметров: ', kwargs)
        f(*args, **kwargs) #вызов функции
        print('Дата и время: ', datetime.datetime.today())
    return wrapper #декоратор возвращает вызов функции-обертки


#Второй декоратор пусть выводит время выполнения декорируемой функции с декоратором:
import time
def args_time_2(f):
    def wrapper():
        start = time.perf_counter_ns()
        f()
        print('Время выполнения кода, ns: ', time.perf_counter_ns() - start)
    return wrapper
#Можно сделать еще так:

decorators = [args_time, args_time_2]
#В качестве декорируемой функции возьмем любую из функций gen...gen4, созданных выше, но с небольшим изменением
#Каскадное применение двух декораторов (сначало выполним args_time, затем args_time_2)
print('\nРезультат каскадного применения декораторов к функции gen: \n')
@decorators[1]
@decorators[0]
def list_gen():
    def gen_new():
        for i in gen_list_1:
            j = i if i > 0 else 0
            yield j
    return print(list(gen_new()))

list_gen() #вызов декорируемой функции, сначало отрабатывает @decorators[0], затем @decorators[0]


#применить задание ultra-pro к остальным задаяним lite и pro не представляется возможным, т.к. в них уже
# были реализованы генераторы и декораторы

#P.S. Какое задание, такое и решение...Надеюсь процесс изменения-доработки контента завершится в самом ближайшем будущем.