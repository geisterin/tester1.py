# имя, фамилия, возраст = input('Введите пожалуйста ваше имя, фамилию и возраст через запятую: ').split(', ')
# #
# # print('Привет ' + имя + ' ' + фамилия + '. Ваш возраст ' + возраст)
# print((f'Привет {имя} {фамилия}. Ваш возраст {возраст}'))

# *********************************************************************************************
#  2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум
#  катетам. (с = sqrt(a * a  +  b * b))
import math
# side_a, side_b = input('Пожалуйста, введите две стороны треугольника, разделенные запятой: ').split(', ')
#
# print(((int(side_a) ** 2) + (int(side_b) ** 2)) ** 0.5)
# # print(math.sqrt(int(side_a ** 2) + (int(side_b) ** 2)))

#**************************
# 3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу,
# которая проверяет, является ли треугольник прямоугольным (с2=a2+b2)
# side_a, side_b, side_c = input('Пожалуйста, введите три стороны треугольника, разделенные запятой: ').split(', ')
#
# if float(side_c) ** 2 == float(side_a) ** 2 + float(side_b) ** 2:
#     print('Triangle is RIGHT')
# else:
#     print('Triangle is NOT RIGHT')

#********************
# Пользователь вводит некоторый произвольный список list. Написать программу, выводящую
# элементы списка в обратном порядке.

# some_list = [1, 2, 5, 67, 8, 4, 3, 8, 9]
# # some_list = input('Please enter some numbers separated by coma: ').split(', ')
# # print(some_list[::-1])
# some_list.reverse()
# print(some_list)
#
# # for num in some_list[::-1]:
# #     print(num)
# ************************************
# Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в
# кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#         Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)

# tupple_1 = (1, 2, 3, 5, 8)
# tupple_2 = (8, 2, 5)
#
# tupple_1 = list(tupple_1)
# for x in tupple_2[::-1]:
#     tupple_1.insert(2, x)
#
# tupple_1 = tuple(tupple_1)
# print(tupple_1)
#*********************
# Написать программу, которая для произвольного списка находит число / числа, наиболее часто
# встречающееся в данном списке и возвращающее их также в виде списка.
#
#         Примеры:
#         [1, 2, 3, 4, 7, 9, 9] → [9]
#         [1, 2, 4, 6, 4, 6] → [4,6]

# test_list1 = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 10]
# empty_dict = {}
# for num in test_list1:
#     empty_dict[num] = test_list1.count(num)
# print(empty_dict)
#
# empty_list = []
# for x in empty_dict.keys():
#     if empty_dict[x] == max(empty_dict.values()):
#         empty_list.append(x)
#
# print(empty_list)

# max_count = 0
# new_list = []
# #
# # print(test_list1.count())
#
# for num in test_list1:
#     if test_list1.count(num) > max_count:
#         max_count = test_list1.count(num)
#
#
# for num in test_list1:
#     if test_list1.count(num) == max_count:
#         new_list.append(num)
#
# new_list = list(set(new_list))
#
# print(new_list)

# #*Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#
#         Примеры:
#         1234565 seconds = 14:6:56:5
# def convert(seconds):
#     print(seconds)
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     print(seconds)
#     hours = seconds // 3600
#     seconds %= 3600
#     print(seconds)
#     minutes = seconds // 60
#     seconds %= 60
#     print(seconds)
#     print(f'{days}:{hours}:{minutes}:{seconds}')
#
#
# user_input = int(input('Please enter amount of seconds'))
# convert(user_input)

