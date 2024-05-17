'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#Задача №1
number = int(input("Введите число:"))
if number >= 0:
    result = number - 10
else:
    result = number + 10
print("Результат:", result)

#Задача №2
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = a * b
if c < 0:
    result = c * -2
else:
    result = c * 3
print("Результат:", result)

#Задача №3
a1 = int(input("Первое число a1:"))
b1 = int(input("Второе число b1:"))
sum = a1 + b1
if sum % 2 == 0:
    result = a1 * b1
else:
    if b1 !=0:
        result = a1 / b1
    else:
      print("Ошибка: деление на ноль!")
      result = None
if result is not None:
    print("Результат:", result)
    
#Задача №4
m = int(input("Первое число m:"))
n = int(input("Второе число n:"))
if m > n:
    result = m - n
else:
    result = n - m
    print("Результат вычитания:", result)
    
#Задача №5
d = int(input("Введите число d:"))
if d > 10:
    result = 1 / 2
else:
    result = 1 * 5
    print("Результат:", result)
    
#Задача о книгах
genre = int(input("Жанр книги:")) 
rating = int(input("Рейтинг книги (от 1 до 5):"))
if genre == "Фантастика" and rating > 4:
    print("Вам следует прочитать эту книгу!")
else:
    print("Может быть,эта книга вам не понравиться")
    
#Задача о здоровом питании
calories = int(input("Количество калорий в продукте:"))
sugar = int(input("Количество сахара в продукте (в граммах):"))
if calories < 200 or sugar < 5:
    print("Этот продукт очень низкокалорный, содержит мало сахара.  Рекомендуется покупать.")
elif calories > 500 and sugar > 10:
    print("Этот продукт очень высококалорийный, содержит много сахара.  Не рекомендуется покупать.")
else:
    print("Этот продукт можно покупать, так как его калорийность и содержание сахара находятся в пределах нормы.")
    
#Задача о бюджете
budget = int(input("Ваш текущий бюджет:"))
price = int(input("Цена товара:"))
necessity = int(input("Необходимость товара (да, нет):"))
if budget >= price:
    if necessity == "Да":
        print("Вы можете позволить купить себе этот товар, он вам необходим.")
    else:
      print("Вы можете позволить купить себе этот товар, но он не является необходимым.")
else:
    if necessity == "Да":
        print("У вас недостаточно средств для покупки необходимого товара.")
    else:
        print("У вас недостаточно средств для покупки этого товара, но он не является необходимым.")
    
#Задача о транспорте
distance = int(input("Расстояние до вашего места назначения в километрах:"))
time = int(input("Текущее время суток в часах (от 0 до 24):"))
if distance < 2 and (time < 6 or time < 22):
    print("Вам следует идти пешком:")
elif distance < 10 and (time < 6 or time < 22):
    print("Вам следует использовать велосипед.")
elif distance < 50:
    print("Вам следует использовать автомобиль или общественный транспорт.")
else:
    print("Вам следует использовать автомобиль.")
    
#Задача о погоде
temperature = int(input("Введите температуру в градусах Цельсия:"))
weather_condition = input("Введите состояние погоды (солнечно, облачно, дождь):")
if temperature > 20 and weather_condition == "солнечно":
    print("Надеть футболку и шорты")
elif temperature > 20 and weather_condition == "облачно":
    print("Надеть брюки и футболку")
elif temperature > 20 and weather_condition == "дождь":
    print("Надеть лёгкую куртку")
elif temperature <= 20 and weather_condition == "солнечно":
    print("Надеть джинсы и рубашку")
elif temperature <= 20 and weather_condition == "облачно":
    print("Надеть джинсы и толстовку")
elif temperature <= 20 and weather_condition == "дождь":
    print("Надеть джинсы и куртку")
else:
    print("Недостаточно данных для выбора одежды")