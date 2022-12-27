#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#      и вывести многочлен степени k. a, b, c, d, e, h - рандом
#     Пример:
# k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
    
from random import randint
k=int(input('Введите натуральное степень K: ')) 

polynomial=str(randint(0,100))+'x' + ' + '+str(randint(0,100))

if k==1:
   print(polynomial)
elif k<1:
    print("Надо было ввести натуральное число. Попробуйте еще раз.")
else:
    koef=[]
    for i in range(k-1):
        koef.append(randint(0,100))
    
    stepeni=[]
    for i in range(2,k+1):
        stepeni.append(i)
  
    for i in range(0,k-1):
        polynomial=str(koef[i])+'x^'+str(stepeni[i])+' + '+polynomial
    print(polynomial)



    







