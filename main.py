'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#Задача №1
P = int(input("Введите число P:"))
numbers = []
i = 2
while True:
    number = i ** 0.5
    if number < P:
       numbers.append(number)
    else:
        break
    i += 1
print("Числа, меньшие", P, "в последовательности корней чисел:")
print(numbers)

#Задача №2
A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A < B:
    for number in range(A + 1, B):
        print(number)
else:
    print("Ошибка: A должно быть меньше B.")
    
#Задача №3
A1 = int(input("Введите число A1: "))
B1 = int(input("Введите число B1: "))
if A1 < B1:
 for i in range(B1 -1, A1 -1):
     print(i)
else:
    print("Ошибка: A1 должно быть меньше B1.")
    
#Задача №4
N = int(input("Введите целое число N (> 1):"))
K = (N + 2) // 3
print(f"Наименьшее целое K, при котором 3 * K > N, равно {K}")
print(f"Значение 3 * K: {3 * K}")

#Задача №5
N1 = int(input("Введите целое число N1 (> 1):"))
K1 = (N1 -1) // 3
print(f"Наибольшее целое K1, при котором 3 * K1 < N1, равно {K1}")


#Задача №1
INCH_TO_CM = 2.54
for inches in range(10, 23):
    centimeters = inches * INCH_TO_CM
    print(f"{inches} дюймов = {centimeters} сантиметров")
    
#Задача №2
kurs = int(input("Введите курс доллара к рублю:"))
for i in range(1, 21):
    rubles = i * kurs
    print(f"{kurs} доллара = {rubles} рублей")
    
#Задача №3
import math

e = 1
for n in range(1, 21):
    e *= n
    print(f"e^{n} = {e}")
    
#Задача №4
start = 1
end = 21
for i in range(start, end + 1):
    print(f"{i}.1")
    
#Задача №5
for i in range(1, 10):
    print(f"2.{i}")