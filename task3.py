# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: 3 1 2 3
# Вывод: 2 1

mylist=[3,1,2,3,3,2,3,2,5,4]
print(f'Задана последовательность чисел {mylist}')

notRepeatList=[]
for element in mylist:
    if mylist.count(element)==1:
        notRepeatList.append(element)
print(notRepeatList)

# Второй вариант решения:

# notRepeatList=[]
# repeatList=[]
# for i in mylist:
#     if i not in repeatList:
#         if i not in notRepeatList:
#             notRepeatList.append(i)
#         else:
#             repeatList.append(i)
#             notRepeatList.remove(i)
# print(f'Список повторяющихся чисел из заданной последовательности {repeatList}')
# print(f'Список неповторяющихся чисел из заданной последовательности {notRepeatList}')


