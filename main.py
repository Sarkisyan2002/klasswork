'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#Задача №1
a = input("Введите пароль раз:")
b = input("Введите пароль второй раз:")
if a == b:
    print("Пароль принят")
else:
    print("Пароль не принят")
    
#Задача #2
c = int(input("Введите целое число:"))
if c %2 ==0:
    print("Чётное")
else:
    print("Нечётное")
    
#Задача #3
n = int(input("Целое положительное четырёхзначное число:"))
l = (n // 10 ** 3) % 10
m = (n // 10 ** 2) % 10
k = (n // 10 ** 1) % 10
d = (n // 10 ** 0) % 10

if l + d == m - k:
    print("ДА")
else:
    print("НЕТ")
    
#Задача №4
age = int(input("Введите возраст пользователя:"))
if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ запрешён")
    
#Задача №5
g = int(input("Введите первое число:"))
i = int(input("Введите второе число:"))
j = int(input("Введите третье число:"))

if i == (g + j) /2:
    print("YES")
else:
    print("NO")