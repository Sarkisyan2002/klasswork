'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#Задача №1
A = int(input("Введите число А, не превышающее по модулю  10000:  "))
B = int(input("Введите число B, не превышающее по модулю 10000:  "))
C = int(input("Введите число С, не превышающее по модулю 10000:  "))
if (A % 2 == 0 & B % 2 != 0) or (A % 2 != 0 & B % 2 == 0):
    print ("yes")
elif (A % 2 == 0 & B % 2 !=0) or (C % 2 !=0 & C % 2 == 0):
    print ("yes")
elif (B % 2 == 0 & C % 2 !=0) or (B % 2 !=0 & C % 2 == 0):
    print ("yes")
else:
    print ("no")
    
#Задача №2
d = int(input("Введите целое число:"))
if d > 0:
    print(1)
elif d < 0:
    print (-1)
else:
    print (0)
    
#Задача №3
a = int(input("Введите число а: "))
b = int(input("Введите число b:"))
c = int(input("Введите число с:"))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    print(a, b, c)
    
#Задача №4
A = int(input("Дано целое число :"))
B = int(input("Дано целое число :"))
C = int(input("Дано целое число :"))
D = int(input("Дано целое число :"))
F = int(input("Дано целое число :"))
if A <= D & B <= F or A <= F & B <= D:
    print("YES")
else:
    if A > B:
        A, B = B, A
if D > F:
    D, F = F, D
if A <= D & B <= F:
    print("Yes")
else:
    print("NO")
    
#Задача №5


M = int(input())
N = int(input())
K = int(input())
P = int(input())
X = int(input())
if M <= P & N <= X or M <= X & N <= P:
    print("YES")
elif K <= P & N <= X or K <= X & N <= P:
    print("YES")
elif M <= P & K <= X or M <= X & N <= P:
    print("YES")
else:
    print("YES")