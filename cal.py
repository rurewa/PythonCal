# Мой первый калькулятор на Python v1.2
# Осуществлена проверка корректности ввода знака оператора
print("Здравуствуйте! Это калькулятор.")
print("Введите по очереди: первое число, оператор и второе число, нажимая Enter")

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
    print("Вы ввели некорректные данные")
    exit(0) # Завершение программы
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print("Введите оператор: +, -, *, /")
operator = str(input())
# Проверка правильности ввода математического оператора
if operator == '+' or operator == '-' or operator == '*' or operator == '/':
    print("Выввели:", operator)
else:
    print("Вы ввели неправильный оператор!")
    exit(0)

second_num = input("Введите второе число: ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Проверка корректности ввода числа
is_num = True 
try:
    float(second_num)
except ValueError:
    is_num = False
if is_num == True:
    second_num = float(second_num)
    print("Вы ввели: ", second_num)
else:
    print("Вы ввели некорректные данные")
    exit(0)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
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