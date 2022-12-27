# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

def multiplPrime(number):
    
    multiple=[]
    k=2

    while number>1:
        for i in range(k,number+1):
            if number%i==0:
                k=i
                number=int(number/i)
                multiple.append(i)
                break
        else:
            return multiple
    
    return multiple
  
n=int(input('Введите натуральное число N: '))  
print(multiplPrime(n))

