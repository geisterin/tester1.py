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

# id_code = input('Введите исикукод: ')
#
# if len(id_code) == 11:
#     print('Ваш исикукод', id_code)
# elif len(id_code) > 11:
#     print('Код длиннее 11 цифр, введите заново')
# else:
#     print('Код короче 11 цифр, введите заново')
#

#*************    УРОК 4 ***************************


# user_input = input('Please enter palendrome: ').lower().replace(' ', '').replace(',', '').replace('.', '').replace('!', '')
#
# if user_input== user_input[::-1]:
#     print('Это палендром')


# empty_list = []
# print(type(empty_list))
#
# world = 'world'
#
# some_list = [123, 0.123, 'Hello', world, True, [1,23,0.434], None]
# print(len(some_list))   #Посчитать количество участников списка
# print(some_list[2]) = 'Planet'    #Можно заменить любые данные в списке (переназначить)
# print(some_list[-3])  # выводит определённую позицию списка  если надо с конца считается с -1
# print(some_list[1:5])   #выводит срез списка с 1 по пятый но на деле с 2го по 4й так каа нумерация с 0
# print(some_list[1:5:2])  #где 2 это шаг через сколько брать срез
# print(some_list[::-1])    #печатает весть список в обратном порядке
# some_list
#
# courses = ['History', 'Programming', 'Nath', 'Literature', 'Physics']
# courses.append('Art')   # метод append добаляет  элементы в конец списка
# courses.insert(1, 'Engliish')   #inser добаляет на указанную позицию элемент
# print(len(courses))      #len пишет длину списка
#
# print(courses)

# courses = ['History', 'Programming', 'Nath', 'Literature', 'Physics']
# courses2 = ['Art','English']
# courses.extend(courses2)             #extend расширяет список в конце
# print(courses)

#
# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
# courses.remove('Math')               # Удаляет из списка математику  remove не запоминает что удалил, не удаляет по названию'Match' а только по порядковому номеру
# print(courses)
#
# deleted = courses.pop(0)                   # Если в скобках не ставить порядковый номер то удаляет последний
# print(courses)
# print(deleted)            # метод *pop* запоминает что удалил

# courses = ['History', 'Programming', 'Nath', 'Literature', 'Physics']
# print(courses)                  #Печатает список в обратном порядке
# courses.reverse()
# print(courses)

# courses = ['History', 'Programming', 'Nath', 'Literature', 'Physics']
# print(courses)
# courses.reverse()        #Все элементы записывает в обратно порядке и сохраняет список в развёрнутом виде
# print(courses)

# courses = ['History', 'Programming', 'Nath', 'Literature', 'Physics']
# print(courses[0])                   #печатает 1 порядковый номер списка т потом первый номер изменённого списка*перевёрнутого-
# courses.reverse()
# print(courses[0])

# courses = ['History', 'Programming', 'Nath', 'Literature', 'Physics']
#
# print(list(reversed(courses)))      #разворачивает список или строку, не сохраняет
# print(courses)
# print(courses[::-1])    #print(list(reversed(courses))) эдентичный способ этому
# print(courses)

# courses = [' History', 'Programming', 'Nath', 'Literature', 'Physics']
# numbers = [1, 4, 6, 8, 2, 3]
# courses.sort()     #Сортирует списки из строк в алфавитном порядке
# print(courses)           # corses.sort(reverse=True) #сортирует в обратном порядке по алфавиту

# numbers.sort()    #Сортирует по порядковому номеру
# print(numbers)

# courses = [' History', 'Programming', 'Nath', 'Literature', 'Physics']
#
# courses.count('History')
# numbers = [1, 4, 6, 8, 2, 3]
# # print(sorted(numbers))        #сортирует по порядковому номеру
# print(sum(numbers))      #суммирует цифровой ряд
# print(min(numbers))             #выводит минимальное значение
# print(max(numbers))             # максимальное значение
#
# courses = (' History', 'Programming', 'Nath', 'Literature', 'Physics')
# print(min(courses))         #работают и со списками строк минимум ближе к букве А
# print(max(courses))         #Максимум ближе к букве Z


# random_list = [[9, 9], [1, 1, 1, 1], [1, 1]]
# print(min(random_list))     #выводит максим и мин элементы листа
# # print(max(random_list))
# courses = (' History', 'Programming', 'Math', 'Literature', 'Physics')
# # print(courses.index('Math'))              # Печатае порядковый номер слова Матч
# # print(courses[courses.index('Math')])     # и выводит значение
# # print('Math' in courses)   #конструкция возвражает булиан если этот элемент если есть в этом списке тру если есть и фолс если нет
# if 'Math' in courses:                #Печатает окей если математика есть в курсе
#     print('OK')
#
# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
# # corses_str = str(courses)     # конвертирует список в строку в том виде какой есть со скобками запятыми и тд
# # print(corses_str)
# courses_str = ' '.join(courses)      # если в апострофе пробелы то строка идёт через пробелы если запятые с пробелами то так и и дёт
# print(courses_str)
# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
# separator = ' '
# courses_str = separator.join(courses)      # если в апострофе пробелы то строка идёт через пробелы если запятые с пробелами то так и и дёт
#
# print(courses_str)
# new_list = courses_str.split()  #обратно переводит строку в лист () это пробел берёт пробулы из строки можно указать как выделить','
# print(new_list)

# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics']
# numbers = [1, 4, 6, 8, 2, 3]
# print(courses + numbers)      #складывает 2 списка
# courses.extend(numbers)     # метод extend так же складывает два списка
# print(courses)


# имеем список создаём копию меняем в одной одно в другой другое значение

# друзья = ['Катя', 'Маша', 'Женя', 'Ира']
#
# друзья2 = друзья.copy()
# print(друзья)
# print(друзья2)
# друзья[0] = 'Мадина'
# друзья2[1] ='Зарина'
# print(друзья)
# print(друзья2)


# цифры = [1, 4, 6, 8, 2, 3, 6, 6, 6, 6]
# print(цифры.count(6))   # метод coint считает сколько у меня таких цифр
#******************************
# элемент  tuple кортеж обозначается круглыми скобками(), не изменяемый

# друзья = ('Катя', 'Маша', 'Женя', 'Ира', 'Катя')
# print(друзья[3])    #выдаёт Иру, переназвать нельзя у кортежа только 2 метода
# print(друзья.count('Катя'))   #сколько раз искомое значение Катя 2 раза
# друзья = ('Катя', 'Маша', 'Женя', 'Ира', 'Ира',)
# друзья2 = ('Зарина', 'Мадина', 'Катя', 'Яна')      #кортеж нелья изменить но можно сложить
# print(друзья + друзья2)     # или создать новый кортеж
# новые_друзья = друзья + друзья2
# print(новые_друзья)

# прочитанные_книги = ('война и мир 1', 'война и мир 2', 'Пайтон для чайников')
# # print(прочитанные_книги)
# прочитанные_книги2 =('Незнайка на луне', 'Му му')
# прочитанные_книги =list(прочитанные_книги)   #конвертировала кортеж в список все методы спика мможно применять
# прочитанные_книги[1] = 'Незнайка на луне'    #индексировала 1 элемент
# прочитанные_книги = tuple(прочитанные_книги)    #снова конвертировала в кортеж
# print(прочитанные_книги)




# x = 5
# student = {'name': 'John', 'age':32, 'courses': ['Math', 'Art', 'Programming'],
#            1: 'int key', 0.2: 'float key', x: 'variable', 'var key': x}
# some_set = {'Art', 'Math'}
# print(student['age'])


# people =['Зина', 'Ира', 'Катя', 'Маша']     #как сделать выборочно не по очереди?
# for person in people:
#     print(person)

#
# ******************************     5урок               ***************
#
#
# for num in range(1, 101):
#     if num % 3 ==0: and num % 5 == 0:     # не доделала доделать!!!!!!!
#     print(num, "FizzBuzz")
#     eli
#         print(num, 'Fizz')
#     elif num % 5 == 0:
#         print(num, 'Buzz')
#     elif num % 3 ==0 and num % 5 ==0:


#
# while True:                  # бесконечная прога
#     print('I can\'t stop')
# condition = True
# cnt = 0
# while condition:
#     if cnt < 1000:
#         print(cnt)
#         cnt = cnt + 1
#     elif cnt ==1000:
#         condition = False
#
#         print('Конец')
# #
#
# condition = True
#
# while condition:
#    user_iput = input('Choiose:\n1: Chek ID\n2: Exit|n--> ')
#    if user_iput == '1':
#        input_id = input('Please enter ID')
#        if len(input_id) != 11:
#            print('Error')
#        else:
#            print(input_id)
#            condition = False
#        elif user_iput == '2':
#            condition = False
#            print('Finished')


# distance_to_target = float(input('Please enter distance in meeters:'))
# current_position = 0
# step = 0
# while current_position = current_position + 0.5
#     step_cnt = step_cnt +1
#     print(current_position)
#
# print('Finished')
# #

#
# some_string = 'Hello world'
#
# print(list(some_string))


# user_input = input('Введите число')
# result = float(user_input ** 2
# print(result)

#
# def user_menu():
#     user_choce = input('Please choose:\n1.Get data by ID code\n/Chec if ID is valid\n3.Exit\n-->')
#     if user_choce =='1':
#         try:
#             user_id = int(input('Please enter ID: '))
#             if len(user_id) != 11:
#                 raise UserWarning
#
#     elif user_choce =='2':
#         pass
#     elif user_choce =='3':
#         quit()
#     else:
#         print('Choise out of range')
#         user_menu()
#
#         def get_data_by_id(idcode):
#             print(idcode)
