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

# a = 'Hello'
# b = 'world'
# print(a + ' ' + b)  #Без пробела в апострофе слова сольются
# print(a + ' ' + 'planet')  # Не только переменные но и слова

#
# name = 'Shimi'
# age = 2
# profession = 'dog'
#
# print('Hello ' + name + '. Your age ' + str(age) + '. Yor are ' + profession + '.')

# name = 'Zina'
# salary = 2500
# string_sample = "Zina's salary is {}"
# print(string_sample.format(salary))


# string_sample = "This {product:} costs {price:} euros"
# print(string_sample.format(price=350, product="Computer"))

#
# string_sample = "This {product:} costs {price:.2f} euros"   #.2f 2 цыфры после .
# print(string_sample.format(price=350, product="Computer"))
#
# emp_name = 'Zina'
# emp_age = 43
# emp_salary = 2500
#
# emp_string = f'Hi, my name is {emp_name}! I  am {emp_age} old. My salary is {emp_salary:.2f}'    # Где .2f означают что 2 цыфры осле точки зарплаты а f вначаде строки значит что строка форматированная
# print(emp_string)

# # байтовые строки код, иероглифы и тд
# byte_string = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_string.decode('utf-16'))



# Управляющие конструкции

# number = 200
# if number == 200:    #где == сравнение где if "если" а нок "то"
#     print('OK')
# else:
#     print('NOK')
#

# number = 200
# if number == 200:                # Усли число = 200 напиши тото а если (2 если) то тото
#     print('Nuber is equal to 100')
# elif number < 100:
#     print('Number is smaller than 100')
# else:
#     print('NOK')

# number = 100
#
# if number == 200:
#     print('Nuber is equal to 200')
# elif number < 100:
#     print('Number is smaller than 100')
# elif number % 2 == 0:         # если остаток при делении на 2 не равен нулю то напечатай
#     print('Whole number')
#
# else:
#     print('NOK')


# number = 90    # тут остановится только на первом правильном дальше не будет смотреть
# # все проверхи сверху вниз как находит первое то останавливается
# if number == 200:
#     print('Nuber is equal to 200')
# elif number < 100:
#     print('Number is smaller than 100')
# elif number % 2 == 0:
#     print('Whole number')
#
# else:
#     print('NOK')


# number = 90
# if number == 200:
#     print('Nuber is equal to 200')
#
# elif number < 100:
#     print('Number is smaller than 100')
#     if number % 2 == 0:
#      print('число равно нулю')     # если строка ближе к началу то не выполняется
#
# else:
#     print('NOK')


# sample_string = 'Hello wo'
# if len(sample_string) >10:   #если строка ровна 11 символам то напиши а если короче то напиши
#
#     print('Long string')
# else:
#    print('Short string')

# id_code = input('Please enter your national id: ')
# if len(id_code)==11:
#     print('Your ID code is', id_code)
# elif len(id_code) > 11:
#     print('Код длинннее')
# else:
#     print('Код короче')
#
# word = input('введите слово')
# if len(word)=


# def reverse(text):
#     return text[::-1]
#
# def is_palindrome(text):
#     return text == reverse(text)
#
# something = input('Введите текст: ')
# if(is_palindrome(something)):
#     print('это палиндром')


# str_text = input('Enter text: ')
# str_text = str_text.replace(" ", "")
# str_text = str_text.replace(",", "")
# str_text = str_text.replace(":", "")
# str_text = str_text.replace("!", "")
# str_text = str_text.replace("?", "")
# str_text = str_text.replace(";", "")
# str_text = str_text.replace(".", "")
# str_text = str_text.lower()
# str_text2 = str_text[::-1]
# if str_text == str_text2:
#     print('It\'s palindrom')
# else:
#     print('It\'s not palindrom')

id_code = input('Введите исикукод: ')

if len(id_code) == 11:
    print('Ваш исикукод', id_code)
elif len(id_code) > 11:
    print('Код длиннее 11 цифр, введите заново')
else:
    print('Код короче 11 цифр, введите заново')
