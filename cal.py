# Мой первый калькулятор на Python v1.4
# Осуществлена проверка корректности ввода знака оператора
print("Здравуствуйте! Это калькулятор.")
print("Введите по очереди: первое число, оператор, второе число, нажимая Enter")         

def err(num): # Функция проверки корректности ввода числа
    is_num = True 
    try:
        float(num)
    except ValueError:
        is_num = False
    if is_num == True:
        num = float(num)
        print("Вы ввели: ", num)
    else:
        print("Это не число!")
        exit(0) # Завершение программы   


first_num = input("Введите первое число: ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Проверка корректности ввода первого числа
err(first_num)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
operator = str(input("Введите оператор: +, -, *, /"))
# Проверка правильности ввода математического оператора
if operator == '+' or operator == '-' or operator == '*' or operator == '/':
    print("Вы ввели:", operator)
else:
    print("Вы ввели неправильный оператор!")
    exit(0)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
second_num = input("Введите второе число: ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Проверка корректности второго ввода числа
err(second_num)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Вычисляем результат
if operator == '+':
    result = float(first_num) + float(second_num)
elif operator == '-':
    result = float(first_num) - float(second_num)
elif operator == '*':
    result = float(first_num) * float(second_num)
else:
    try: # Обработка ошибки деления на 0
        result = float(first_num) / float(second_num) 
    except ZeroDivisionError:
        print("На 0 делить нелья!")
        exit(0) # Завершение программы   
        
print("Результат вычисления", result)
