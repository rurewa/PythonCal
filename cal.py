# Мой первый калькулятор на Python
print("Здравуствуйте! Это калькулятор.")
print("Введите по очереди два числа")
print("Введите первое число: ")
first_num = float(input())
print("Введите второе число")
second_num = float(input())
print("Введите оператор: +, -, *, /")
operator = str(input())
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
     
