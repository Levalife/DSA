# -*- coding: utf-8 -*-

# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets,
# evaluate the expression. Assume the expression is properly formed.

# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4
# Here's the function signature:


def eval(expression):
    '''
    Time O(n)
    '''

    operators = []
    operands = []

    operators_set = {'+', '-', '*', '/'}

    for e in expression:
        if e == ')':
            b = int(operands.pop())
            a = int(operands.pop())
            op = operators.pop()

            operands.append(perform_operation(a, b, op))

        elif e != '(':
            if e in operators_set:
                operators.append(e)
            else:
                operands.append(e)

    while operators:

        a = int(operands.pop(0))
        b = int(operands.pop(0)) if operands else 0
        if not b:
            a, b = b, a
        op = operators.pop(0)
        operands.insert(0, perform_operation(a, b, op))
    return operands.pop()


def perform_operation(a, b, op):
    c = None
    if op == '+':
        c = a.__add__(b)
    elif op == '-':
        c = a.__sub__(b)
    elif op == "*":
        c = a.__mul__(b)
    elif op == '/':
        c = a.__truediv__(b)
    return c

print(eval('-(3+(2-1))'))
# -4
print(eval('(((2-3)+3)-1)'))
# 1
print(eval('(2-(3+2))'))
# -3
print(eval('2-(3+2)'))
# -3
print(eval('(3+2)*2'))
# 10
print(eval('(3+2)*(1+1)'))
# 10
print(eval('(3+2)*(1+1)*(1+1)'))
# 20
print(eval('(2+8)*(1+1)/(1+3)'))
# 5

