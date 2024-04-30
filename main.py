'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#Задача №6
a = int(input("Введите длину стороны a:"))
b = int(input("Введите длину стороны b:"))
c = int(input("Введите длину стороны c:"))
if a == b == c:
    print("равносторонний")
elif (a == b or a == c or b == c) and (a !=b or a !=c or b !=c):
    print("равнобедренный")
elif a !=b and a !=c and b !=c:
    print("разносторонний")
    
#Задача №7
print("Координаты точки: ")
x = int(input("x = "))
y = int(input("y = "))
if x > 0 and y > 0:
    print("точка в первой четверти")
elif x < 0 and y > 0:
    print("точка во второй четверти")
elif x < 0 and y < 0:
    print("точка в третьей четверти")
elif x > 0 and y < 0:
    print("точка в четвёртой четверти")
elif x == 0 and y == 0:
    print("точка в центре координат")
elif x == 0:
    print("точка на оси x")
elif y == 0:
    print("точка на оси y")
    
#Задача №8
a = int(input("Введите номер месяца a = :"))
if a == 12 or a == 1 or a == 2:
    print('winter')
elif a == 3 or a == 4 or a == 5:
    print('spring')
elif a == 6 or a == 7 or a == 8:
    print('sammer')
elif a == 9 or a == 10 or a == 11:
    print('autumn')
else:
    print("Error")
    
#Задача №9
temperature = int(input("Введите температуру: "))
if temperature >= 35:
    print ("На улице очень жарко, рекомендуется под солнцем не стоять и пить побольше воды")
elif temperature >= 20:
    print ("На улице тепло, можно надеть шорты и футболку")
elif temperature >= 10:
    print ("На улице прохладно, лучше надеть джинсы и толстовку")
else:
    print ("На улице холодно, надо одеть куртку и шапку")
    
#Задача №10
x = int(input("Введите координату x точки: "))
y = int(input("Введите координату y точки:"))
x1 = int(input("Введите координату x1 верхнего левого угла прямоугольника:"))
y1 = int(input("Введите координату y1 верхнего левого угла прямоугольника:"))
x2 = int(input("Введите координату x2 нижнего правого угла прямоугольника:"))
y2 = int(input("Введите координату y2 нижнего правого угла прямоугольника:"))
if x1 <= x <= x2 and y1 <= y <= y2:
    print("Точка находится внутри прямоугольника")
else:
    print("Точка находится вне прямоугольника")