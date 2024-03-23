'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#Задача №1
a = int(input("Введите целое число a:"))
b = int(input("Введите целое b:"))
if a > b:
    print ("Число a больше!")
else:
    print ("Число b больше!")
    
#Задача №2
year = int(input("Введите год:"))
if year % 4 != 0:
    print ("NO")
elif year % 100 == 0:
    if year % 400 == 0:
        print ("Yes")
else:
    print ("No")
    
#Задача №3
n = int(input("Введите число n:"))
m = int(input("Введите число m:"))
k = int(input("Введите число k:"))
if ((n + m) > k) & ((n + k) > m & ((m + k) >n)):
    print ("Yes")
else:
    print ("No")
