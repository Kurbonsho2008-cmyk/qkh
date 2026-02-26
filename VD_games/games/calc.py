"""Игра 'Калькулятор'"""

import random
import operator

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op_symbol = random.choice(list(OPERATIONS.keys()))
    
    correct_answer = OPERATIONS[op_symbol](num1, num2)
    question = f"{num1} {op_symbol} {num2}"
    
    return question, correct_answer
