# number = 500
# number2 = 500.0
# text_string = '500'
#
# print(help(number))
#
# number = 500  #Integer
# number2 = 500.0  # Float
# text_string = 'Hello zina'  #String
# boolean_var = True  # Boolean
# none_type = None  # None type
# a = 500
# b = 200
#
# print(a+b)
# print(500 + 200)
# print(a + 1000 + b)


# a = 500
# b = 200
# print(a / b)
# print(type(a / b))


# sample_string = 'Hello world'
# print(sample_string)

# string_sample = 'Hello world'
# print(string_sample[10])

#
# empty_string = ''
# string_sample = "Hello world"
# string_sample2 = "first letteR is lowErcase"
# string_sample3 = " extra whitespace string "
#
# print(string_sample.upper())

#
# a = 'Hello'
# b = 'world'
#
# print(a + ' ' + b) #печатает первую и вторую строку

# sample_string = 'Hello world'
# print(sample_string)  # Напечатать строку


# string_sample = 'Privet Geisterin'
# print(string_sample[0])  #Первый символ

#
# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# print(len(string_sample))
# print(len(numbers))
#
# print(string_sample[26]) #сколько символов в предложени и последний символ


# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# print(len(string_sample))
# print(len(numbers))
#
# print(string_sample[0:8])    # отображаются первый 8 букв

# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# numbers2=''
#
# print(string_sample[-1])    # отображается последний знак

#
# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# numbers2=''
#
# print(string_sample[-6:-1])     # последний символне отображается
# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# numbers2=''
#
# print(string_sample[-6:]) # с -6 до конца

# Положительная индексация начинается с 0 Отрицательная начинается с -1



# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# numbers2=''
#
# print(string_sample[0:26:2])  #0 значит с первого символа, 26 количество символов в предложении, 2 это шаг индексации.


# string_sample = 'Privet Geisterin, kak dela?'
# numbers = '12345678'
# numbers2=''
#
# print(string_sample[::-1])    # Первое : с конца втрое : до начала  -1 шаг с конца


# string_sample = 'Hello world'
# numbers ='12345678'
# numbers2 = '-6-5-4-3-2-1'
# new_string = string_sample[::-1]
# print(new_string)     #Сохранение новой строки полностью:: с начала до конца -1 наоборот
# print(string_sample)  #Напечатай строку стринг_сэмпл


# empty_string = ''
# string_sample = "Hello world world"  # Два слова ворлд
# string_sample2 = "first letteR is lowErcase"    # Заглавные и строчные перепутаны
# string_sample3 = " extra whitespace string "  # два пробела в начале и в конце
# print(len(string_sample))   # Количество символов строки
# print(string_sample.upper())   # upper - большими буквами метод апер
# string_sample = string_sample.upper()  # строка такаято = строке большими буквами
# print(string_sample)
# print(string_sample.lower())   #Строка приводит все буквы в прописные

# name_sample = 'zinA RoManovA'   # имя введены разными регистрами
# print(name_sample.capitalize())   #все буквы делает строчными и первую Большой
# print(string_sample3.strip())      #Удаляяет пробелы спереди и сзади лишние
# print(string_sample3.strip('.'))   # удаляет точку вначале и вконце только 1й и последний символо строки
#

# empty_string = ''
# string_sample = "Hello world world"  # Два слова ворлд
# string_sample2 = "first letteR is lowErcase"    # Заглавные и строчные перепутаны
# string_sample3 = " extra whitespace string "
# user_input = input('Please enter something: ')  # ДЛЯ ДОМАШКИ
# user_input = string_sample.split()   # метод сплит разделяет строку в другой тип данных в список.
# print(user_input)
# print(string_sample.count('world'))  # метонд коунт считает сколько раз появляется данное слово, знак, буква, символ если в апострофах пусто то количество символов

# print(string_sample.find('world'))  # Находит место где находится ворлд и выводит позицию в строке, находит первое совпадение
# print(string_sample[6:])

# empty_string = ''
# string_sample = "Hello world world"  # Два слова ворлд
# string_sample2 = "first letteR is lowErcase"    # Заглавные и строчные перепутаны
# string_sample3 = " extra whitespace string "
#
# print(string_sample.find('world'))
# print(string_sample[6:11])
# print(string_sample[11:].find('world'))  #индексирует, находиит место первого слова ворлд и с него ищет ещё одно место и находит на 1 месте относительно первого среза


# empty_string = ''
# string_sample = "Hello world world"
# print('world' in string_sample)   # Осуществляется прооверка существует ли такое слово в данной строке
#

a = 'Hello'
b = 'world'
print(a + ' ' + b)  #Без пробела в апострофе слова сольются
print(a + ' ' + 'planet')  # Не только переменные но и слова



