<<<<<<< HEAD
# Мой первый калькулятор на Python. V1.1
print("Здравуствуйте! Это калькулятор.")
print("Введите по очереди два числа")
print("Введите первое число: ")
first_num = float(input())
print("Введите оператор: +, -, *, /")
operator = str(input())
print("Введите второе число")
second_num = float(input())
# Условие для проверки корректности ввода оператора
if operator == '+' or operator == '-' or operator == '*' or operator == '/':
    if operator == '+':
        result = first_num + second_num
        print("Результат сложения", result)
    elif operator == '-':
        result = first_num - second_num
        print("Результат вычитания: ", result)
    elif operator == '*':
        result = first_num * second_num
        print("Результат произведени: ", result)
    else:
        result = first_num / second_num
        print("Результат деления: ", result)
else:
    print("Вы ввели неверный оператор!")
=======
# Мой первый калькулятор на Python v1.3
# Осуществлена проверка корректности ввода знака оператора
print("Здравуствуйте! Это калькулятор.")
print("Введите по очереди: первое число, оператоб, второе число, по очереди, нажимая Enter")

first_num = input("Введите первое число: ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Проверка корректности ввода первого числа
is_num = True 
try:
    float(first_num)
except ValueError:
    is_num = False
if is_num == True:
    first_num = float(first_num)
    print("Вы ввели: ", first_num)
else:
    print("Это не число!")
    exit(0) # Завершение программы
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print("Введите оператор: +, -, *, /")
operator = str(input())
# Проверка правильности ввода математического оператора
if operator == '+' or operator == '-' or operator == '*' or operator == '/':
    print("Вы ввели:", operator)
else:
    print("Вы ввели неправильный оператор!")
    exit(0)

second_num = input("Введите второе число: ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Проверка корректности второго ввода числа
is_num = True 
try:
    float(second_num)
except ValueError:
    is_num = False
if is_num == True:
    second_num = float(second_num)
    print("Вы ввели: ", second_num)
else:
    print("Это не число!")
    exit(0)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Вычисляем результат
if operator == '+':
    result = first_num + second_num
    print("Результат сложения", result)
elif operator == '-':
    result = first_num - second_num
    print("Результат вычитания: ", result)
elif operator == '*':
    result = first_num * second_num
    print("Результат произведени: ", result)
else:
    if second_num == 0:
        print("На ноль делить нельзя!")
    else:    
        result = first_num / second_num
        print("Результат деления: ", result)
>>>>>>> ddc29b8dc6791e64a7e3773bc8d02b244c3e1a4e
