# chk_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# chk_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#
# id_code = '38803160272'
#
#
# result = 0
# for num in range(0, 10):
#     result += chk_1[num] * int(id_code[num])
#
# if result % 11 != id_code[-1]:
#     result = 0
#     for num in range(0, 10):
#         result += chk_2[num] * int(id_code[num])
#     if result % 11 ==int(id_code[-1]):
#         print('ID Code is valid')
#     else:
#         print('ID Code is not valid')
# else:
#     print('ID Code is valid')
