# Вычисление числа, слева от указанной позиции
def backward_digit(user_expression, pos):
    pos -= 1
    digit = ''
    while pos>= 0  and not user_expression[pos] in ['+', '-', '*', '/', '(', ')']:
        digit = user_expression[pos] + digit
        pos -= 1
    if user_expression[pos] == '-':
        digit = '-' + digit
    return digit

# Вычисление числа, справа от указанной позиции
def forward_digit(user_expression, pos):
    pos += 1
    digit = ''
    while pos <= len(user_expression)-1 and not user_expression[pos] in ['+', '-', '*', '/', '(', ')']:
        digit = digit + user_expression[pos]
        pos += 1
    return digit

# Замена в строке двух чисел на их частное для первой найденной операции деления
def div_operation(user_expression):
    if '/' in user_expression:
        pos = user_expression.index("/")
        b = backward_digit(user_expression, pos)
        f = forward_digit(user_expression, pos)
        result = float(backward_digit(user_expression, pos))/float(forward_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression

# Замена в строке двух чисел на их произведение для первой найденной операции умножения
def mult_operation(user_expression):
    if '*' in user_expression:
        pos = user_expression.index("*")
        b = backward_digit(user_expression, pos)
        f = forward_digit(user_expression, pos)
        result = float(backward_digit(user_expression, pos))*float(forward_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression

# Замена в строке двух чисел на их сумму для первой найденной операции сложения
def sum_operation(user_expression):
    if '+' in user_expression:
        pos = user_expression.index("+")
        b = backward_digit(user_expression, pos)
        f = forward_digit(user_expression, pos)
        result = float(backward_digit(user_expression, pos))+float(forward_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression

# Замена в строке двух чисел на их разность для первой найденной операции вычитания
def dif_operation(user_expression):
    if '-' in user_expression:
        pos = user_expression[1:].index("-")+1
        b = backward_digit(user_expression, pos)
        f = forward_digit(user_expression, pos)
        result = float(backward_digit(user_expression, pos))-float(forward_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression

# Вычисление любого выражения без скобок
def eval_simple_expression(simple_expression):
    while '/' in simple_expression:
        simple_expression = div_operation(simple_expression)
    while '*' in simple_expression:
        simple_expression = mult_operation(simple_expression)
    while '+' in simple_expression:
        simple_expression = sum_operation(simple_expression)
    while '-' in simple_expression[1:]:
        simple_expression = dif_operation(simple_expression)
    return simple_expression

# Нахождение первого по приоритету вычисления выражения в скобках и вычисление его
def eval_bracket_expression(user_expression):
    left_pos = 0
    right_pos = 0
    for i in range(len(user_expression)):
        if user_expression[i] == '(':
            left_pos = i
        if user_expression[i] == ')':
            right_pos = i
            if left_pos == 0:
                left_part = ''
            else:
                left_part = user_expression[:left_pos]
            if right_pos == len(user_expression)-1:
                right_part = ''
            else:
                right_part = user_expression[right_pos+1:]

            user_expression = left_part + eval_simple_expression(user_expression[left_pos+1:right_pos]) + right_part
            return user_expression
    return user_expression

# Проверка правильно ли расставлены скобки в выражении
def is_bracket_ok(user_expression):
    b_count=0
    for i in range(len(user_expression)):
        if user_expression[i] == '(':
            b_count += 1
        if user_expression[i] == ')':
            b_count -= 1
        if b_count<0:
            return b_count
    return b_count

# тело программы
def rational_calc(user_expression):
    try:
         if is_bracket_ok(user_expression) == 0:
             while '(' in user_expression:
                 user_expression = eval_bracket_expression(user_expression)
             user_expression = eval_simple_expression(user_expression)
             return round(float(user_expression),5)
         else:
             return('Не соответствие открытых и закрытых скобок')
    except Exception as err:
        return('Возникла ошибка: ', str(err.args))
    
def complex_calc(user_expression):
    try:
        return eval(user_expression)
    except Exception as err:
        return('Возникла ошибка: ', str(err.args))
